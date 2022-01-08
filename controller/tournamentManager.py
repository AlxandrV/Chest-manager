import json

from controller.stageManager import StageManager as sm
from model.tournament import Tournament as t
from controller.databaseManager import DatabaseManager as dbm
from view.tournamentView import TournamentView as tv
from controller.playerManager import PlayerManager as pm


class TournamentManager:

    def __init__(self) -> None:
        self.TABLE_NAME = "tournament"
        self.s_manager = sm()
        self.t_view = tv()
        self.p_manager = pm()
        self.db_manager = dbm()

    def new_tournament(self) -> None:
        """Creat a new tournament"""
        specifications_new_tournament = self.t_view.new_tournament()
        create_p = self.t_view.create_players()

        if create_p == 1:
            list_p_object = self.p_manager.get_players(specifications_new_tournament['_number_players'])
            list_p_id = [id_player._id for id_player in list_p_object]
            specifications_new_tournament['_list_players'] = list_p_id

        new_tournament = t(specifications_new_tournament)
        self.db_manager.insert_into_db(self.TABLE_NAME, new_tournament)
        id_tournament = self.db_manager.last_insert(self.TABLE_NAME)

        list_id_stage = []
        for number_stage in range(specifications_new_tournament['_stage']):
            list_id_stage.append(self.s_manager.create_stage({
                "_number": number_stage+1,
                "_id_tournament": id_tournament}))
        new_tournament._id_stage = list_id_stage
        self.update_tournament_db(new_tournament, id_tournament)
        self.t_view.except_value("\nNouveau tournoi créé !\n")

    def launch_stage_tournament(self) -> None:
        """Launch a tournament where status is not launched"""
        tournaments = self.get_status_of_tournament([0, 1])
        tournament = self.tournament_to_launch(tournaments)

        if tournament is True:
            return True
        elif tournament is False:
            self.launch_stage_tournament()

        if hasattr(tournament, '_list_players') is False:
            self.t_view.except_value(
                "\nPas de joueurs enregistré pour ce tournoi !\n"
                "Veuillez en ajouter :")
            list_p_object = self.p_manager.get_players(tournament._number_players)
            tournament._list_players = [player._id for player in list_p_object]
            self.update_tournament_db(tournament, tournament._id)
        else:
            list_p_object = self.hydrate_list_players(tournament._list_players)

        sorted_id_stage = sorted(tournament._id_stage)
        for stage_id in sorted_id_stage:
            stage = self.s_manager.search_stage_by_id(stage_id)
            if stage._status == 1:
                self.t_view.except_value(f"\nVeuillez mettre fin au tour n°{stage._number} du tournoi {stage._id}, avant d'en lancer un nouveau !\n")
                break
            elif stage._status == 0:
                self.s_manager.stage_to_launch(stage, list_p_object)
                tournament._stage_in_progress = stage._number
                tournament._status = 1
                self.update_tournament_db(tournament, tournament._id)
                break

    def close_stage_of_tournament(self):
        """Launch a tournament where status is in progress"""
        tournaments = self.get_status_of_tournament([1])
        tournament = self.tournament_to_launch(tournaments)

        if tournament is True:
            return True
        self.s_manager.close_stage(tournament._id)
        tournament._stage_in_progress += 1
        if tournament._stage_in_progress == len(tournament._id_stage):
            tournament._status = 2
        else:
            tournament._status = 1
        self.update_tournament_db(tournament, tournament._id)

    def get_status_of_tournament(self, list_status):
        """Return a list of tournaments by status"""
        tournament_status_object = []
        for status in list_status:
            tournament_status = self.db_manager.search_where(self.TABLE_NAME, '_status', status)
            for tournament in tournament_status:
                tournament_status_object.append(self.hydrate_object_with_json(tournament))

        self.t_view.print_list_tournament_in_progess(tournament_status_object)
        return tournament_status_object

    def list_tournament(self) -> None:
        """List all tournaments"""
        self.get_status_of_tournament([2, 1, 0])

    def tournament_to_launch(self, list_tournament):
        """Return tournament where ID is in list"""
        id_tournament_to_launch = self.t_view.launch_stage_tournament()

        if id_tournament_to_launch in [str(tournament._id) for tournament in list_tournament]:
            for tournament in list_tournament:
                if id_tournament_to_launch == str(tournament._id):
                    return tournament
        elif id_tournament_to_launch == "q":
            return True
        else:
            self.t_view.except_value("ID incorrect")
            return False

    def tournament_report(self):
        """Genrate a report of tournaments"""
        tournaments = self.get_status_of_tournament([2, 1, 0])
        tournament = self.tournament_to_launch(tournaments)
        if tournament is False:
            return self.tournament_report()
        elif tournament is True:
            return True
        resut = self.s_manager.stage_report(tournament)
        if resut is True:
            return self.tournament_report()

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate tournament object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=t)

    def hydrate_list_players(self, list_p_id):
        """Return a list player object"""
        list_p = []
        for id_player in list_p_id:
            list_p.append(self.p_manager.hydrate_object_by_id(id_player))
        return list_p

    def update_tournament_db(self, object_to_update, id_to_object):
        """Update a tournament in database"""
        datas_serialize = self.db_manager.serialize_object_to_json(object_to_update)
        self.db_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)
