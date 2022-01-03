from datetime import time
import json

from prettytable import PrettyTable

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

        specifications_new_tournament['_id_stage'] = []
        for number_stage in range(specifications_new_tournament['_stage']):
            specifications_new_tournament['_id_stage'].append(self.stage_manager.create_stage({"_number": number_stage+1}))

        create_players = self.tournament_view.create_players()

        if create_players == 1:
            list_players_object = self.add_list_players(specifications_new_tournament['_number_players'])
            list_players_id = [id_player._id for id_player in list_players_object]

            specifications_new_tournament['_list_players'] = list_players_id

        new_tournament = t(specifications_new_tournament)
        self.database_manager.insert_into_db(self.TABLE_NAME, new_tournament)

        self.tournament_view.except_value("\nNouveau tournoi créé !\n")
        # sorted_list_players = self.player_manager.sorted_players(list_players)
        
    def list_tournament(self) -> None:
        """List of tournaments"""
        list_tournament = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_tournament_object = []
        for tournament in list_tournament:
            list_tournament_object.append(self.hydrate_object_with_json(tournament))
        self.print_list_tournament(list_tournament_object)


    def launch_tournament(self) -> None:
        """List a tournament in progress and launch"""
        tournament_in_progress = self.database_manager.search_where(self.TABLE_NAME, '_status', False)
        list_tournament_in_progress = []
        for tournament in tournament_in_progress:
            list_tournament_in_progress.append(self.hydrate_object_with_json(tournament))
        self.print_list_tournament(list_tournament_in_progress)

        id_tournament_to_launch = self.tournament_view.launch_tournament()

        if id_tournament_to_launch in [tournament._id for tournament in list_tournament_in_progress]:
            for tournament in list_tournament_in_progress:
                if id_tournament_to_launch == tournament._id:
                    tournament_object = tournament
            self.tournament_to_launch(tournament_object)
        else:
            self.tournament_view.except_value("ID incorrect")
            self.launch_tournament()

    def tournament_to_launch(self, tournament):
        """Launch a tournament"""
        if self.has_attribute(tournament, '_list_players') == False:
            self.tournament_view.except_value(
                "\nPas de joueurs enregistré pour ce tournoi !\n"
                "Veuillez en ajouter :")
            list_players_object = self.add_list_players(tournament._number_players)
            list_players_id = [id_player._id for id_player in list_players_object]
            setattr(tournament, '_list_players', list_players_id)
            self.update_tournament_db(tournament, tournament._id)

        else:
            list_players_object = self.hydrate_list_players(tournament._list_players)

        sorted_id_stage = sorted(tournament._id_stage)
        for stage in sorted_id_stage:
            stage = self.stage_manager.launch_stage(stage, list_players_object)
            if stage != None:
                self.stage_manager.stage_to_launch(stage, list_players_object)
                break

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
        if hasattr(object_with_attr, nam_attr):
            return True
        else:
            return False

    def add_list_players(self, number_to_range):
        """Return a list players object"""
        list_id_players = []
        for player in range(number_to_range):
            new_player = self.player_manager.add_player()
            list_id_players.append(new_player)
        return list_id_players

    def update_tournament_db(self, object_to_update, id_to_object):
        """Update a tournament in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)

    def print_list_tournament(self, list_tournament):
        table_list_tournament = PrettyTable(["ID", "Nom", "Lieu", "Date début", "Date fin", "Contrôle du temps", "Status"])
        
        for element in list_tournament:
            if element._time_control == 1:
                time_control = "Bullet"
            elif element._time_control == 2:
                time_control = "Blitz"
            elif element._time_control == 3:
                time_control == "Coup rapide"
            else:
                time_control = "Error"

            if element._status == False:
                status = "En cours"
            else:
                status = "Déjà joué"

            table_list_tournament.add_row([
                element._id, 
                element._name, 
                element._place, 
                element._date_start, 
                element._date_end,
                time_control,
                status])

        self.tournament_view.except_value(table_list_tournament)