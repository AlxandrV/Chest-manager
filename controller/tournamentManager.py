import json

from controller.stageManager import StageManager as sm
from model.tournament import Tournament as t
from controller.databaseManager import DatabaseManager as dbm
from view.tournamentView import TournamentView as tv
from controller.playerManager import PlayerManager as pm

class TournamentManager:

    def __init__(self) -> None:
        self.TABLE_NAME = "tournament"
        self.stage_manager = sm()
        self.tournament_view = tv()
        self.player_manager = pm()
        self.database_manager = dbm()
    
    def new_tournament(self) -> None:
        """Creat a new tournament"""
        specifications_new_tournament = self.tournament_view.new_tournament()
        create_players = self.tournament_view.create_players()

        if create_players == 1:
            list_players_object = self.player_manager.list_players(specifications_new_tournament['_number_players'])
            list_players_id = [id_player._id for id_player in list_players_object]

            specifications_new_tournament['_list_players'] = list_players_id

        new_tournament = t(specifications_new_tournament)
        self.database_manager.insert_into_db(self.TABLE_NAME, new_tournament)
        id_tournament = self.database_manager.last_insert(self.TABLE_NAME)

        list_id_stage = []
        for number_stage in range(specifications_new_tournament['_stage']):
            list_id_stage.append(self.stage_manager.create_stage({
                "_number": number_stage+1,
                "_id_tournament": id_tournament}))
        new_tournament._id_stage = list_id_stage
        self.update_tournament_db(new_tournament, id_tournament)
        self.tournament_view.except_value("\nNouveau tournoi créé !\n")

    def launch_stage_tournament(self) -> None:
        """Launch a tournament where status is not launched"""
        tournament = self.get_status_of_tournament(0)

        if self.has_attribute(tournament, '_list_players') == False:
            self.tournament_view.except_value(
                "\nPas de joueurs enregistré pour ce tournoi !\n"
                "Veuillez en ajouter :")
            list_players_object = self.player_manager.list_players(tournament._number_players)
            list_players_id = [id_player._id for id_player in list_players_object]
            setattr(tournament, '_list_players', list_players_id)
            self.update_tournament_db(tournament, tournament._id)
        else:
            list_players_object = self.hydrate_list_players(tournament._list_players)

        sorted_id_stage = sorted(tournament._id_stage)
        for stage_id in sorted_id_stage:
            stage = self.stage_manager.search_stage_by_id(stage_id)
            if stage._status == 1:
                self.tournament_view.except_value(f"\nVeuillez mettre fin au tour n°{stage._number} du tournoi {stage._id}, avant d'en lancer un nouveau !\n")
                break
            elif stage._status == 0:
                self.stage_manager.stage_to_launch(stage, list_players_object)
                tournament._stage_in_progress = stage._number
                tournament._status = 1
                self.update_tournament_db(tournament, tournament._id)
                break


    def close_stage_of_tournament(self):
        """Launch a tournament where status is in progress"""
        tournament = self.get_status_of_tournament(1)
        self.stage_manager.close_stage(tournament._id)
        if tournament._stage_in_progress == len(tournament._id_stage):
            tournament._status = 2
        else:
            tournament._status = 0
        self.update_tournament_db(tournament, tournament._id)


    def get_status_of_tournament(self, status):
        """Return a list of tournaments by status"""
        tournament_status = self.database_manager.search_where(self.TABLE_NAME, '_status', status)
        tournament_status_object = []
        for tournament in tournament_status:
            tournament_status_object.append(self.hydrate_object_with_json(tournament))
        
        self.tournament_view.print_list_tournament_in_progess(tournament_status_object)
        return self.tournament_to_launch(tournament_status_object, status)

    def list_tournament(self) -> None:
        """List of tournaments"""
        list_tournament = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_tournament_object = []
        for tournament in list_tournament:
            list_tournament_object.append(self.hydrate_object_with_json(tournament))
        self.tournament_view.print_list_tournament_in_progess(list_tournament_object)


    def tournament_to_launch(self, list_tournament, status):
        """Return tournament where ID is in list"""
        id_tournament_to_launch = self.tournament_view.launch_stage_tournament()

        if id_tournament_to_launch in [tournament._id for tournament in list_tournament]:
            for tournament in list_tournament:
                if id_tournament_to_launch == tournament._id:
                    return tournament
        else:
            self.tournament_view.except_value("ID incorrect")
            self.get_status_of_tournament(status)

    def tournament_report(self):
        list_tournament = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_tournament_object = []
        for tournament in list_tournament:
            tournament = self.hydrate_object_with_json(tournament)
            if tournament._status == 1 or tournament._status == 2:
                list_tournament_object.append(tournament)
        self.tournament_view.print_list_tournament_in_progess(list_tournament_object)
        id_tournament = self.tournament_view.launch_stage_tournament()

        if id_tournament == "q":
            return True
        else:
            try:
                id_tournament = int(id_tournament)
            except ValueError as e:
                self.tournament_view.except_value("Valeur incorrect !\n")
                return self.tournament_report()
        for tournament in list_tournament_object:
            if tournament._id == id_tournament:
                resut = self.stage_manager.stage_report(tournament)
                if resut == True:
                    self.tournament_report()

                

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate tournament object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=t)

    def hydrate_list_players(self, list_players_id):
        """Return a list player object"""
        list_players = []
        for id_player in list_players_id:
            list_players.append(self.player_manager.hydrate_object_by_id(id_player))
        return list_players

    def has_attribute(self, object_with_attr, nam_attr):
        """Verify is has attribute"""
        if hasattr(object_with_attr, nam_attr):
            return True
        else:
            return False

    def update_tournament_db(self, object_to_update, id_to_object):
        """Update a tournament in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)
