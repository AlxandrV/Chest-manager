import json

from datetime import datetime

from model.stage import Stage as s
from controller.playerManager import PlayerManager as pm
from controller.databaseManager import DatabaseManager as dbm
from controller.matchManager import MatchManager as mm
from view.stageView import StageView as sv

class StageManager:

    def __init__(self) -> None:
        self.player_manager = pm()
        self.database_manager = dbm()
        self.match_manager = mm()
        self.stage_view = sv()
        self.TABLE_NAME = "stage"
    
    def create_stage(self, specifications):
        """Create and storage in database Stage and return ID"""
        stage = s(specifications)
        self.database_manager.insert_into_db(self.TABLE_NAME, stage)
        return self.database_manager.last_insert(self.TABLE_NAME)

    def search_stage_by_id(self, id_stage) -> object:
        """Return a stage by ID"""
        stage_json = self.database_manager.search_single(self.TABLE_NAME, id_stage)
        stage = self.hydrate_object_with_json(stage_json)
        return stage
    
    def search_stage_by_condition(self, key, value):
        """Search in database by condition"""
        stage_json = self.database_manager.search_where(self.TABLE_NAME, key, value)
        stages = [self.hydrate_object_with_json(stage) for stage in stage_json]
        for stage in stages:
            if stage._status == 1:
                return stage

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate tournament object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=s)

    def stage_to_launch(self, stage, list_players):
        """Generate list match for a stage"""
        list_pairs_players = self.player_manager.generate_pairs(list_players)

        list_id_match = []
        for i in range(len(list_pairs_players)):
            list_id_match.append(self.match_manager.create_match(stage._id, i+1, list_pairs_players[i-1]))
        stage._list_id_match = list_id_match
        stage._status = 1
        dt = datetime.now()
        stage._datetime_start = dt.strftime('%x %X')
        self.update_stage_db(stage, stage._id)
        self.stage_view.except_value(f"\nDébut du tours n°{stage._number} :\n")

    def close_stage(self, id_tournament):
        """Enter the result of match and close a stage in progress"""
        stage = self.search_stage_by_condition('_id_tournament', id_tournament)
        dt = datetime.now()
        stage._datetime_end = dt.strftime('%x %X')
        self.match_manager.close_stage(stage._id)
        stage._status = 2
        self.update_stage_db(stage, stage._id)

    def stage_report(self, tournament):
        list_stage = self.database_manager.search_where(self.TABLE_NAME, "_id_tournament", tournament._id)
        list_stage_object = []
        for stage in list_stage:
            list_stage_object.append(self.hydrate_object_with_json(stage))
        self.stage_view.print_list_stage(list_stage_object)
        id_stage = self.stage_view.select_stage()

        if id_stage == "q":
            return True
        else:
            try:
                id_stage = int(id_stage)
            except ValueError as e:
                self.tournament_view.except_value("Valeur incorrect !\n")
                return self.stage_report()

        for stage in list_stage_object:
            if stage._id == id_stage:
                list_players = self.player_manager.get_players_in_stage(tournament._list_players)
                result = self.match_manager.match_report(stage, list_players)
                if result == True:
                    self.stage_report(tournament)

    def update_stage_db(self, object_to_update, id_to_object):
        """Update a tournament in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)

