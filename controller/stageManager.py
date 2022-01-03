import json

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

    def launch_stage(self, id_stage) -> object:
        """Launch a stage and generate a match"""
        stage_json = self.database_manager.search_single(self.TABLE_NAME, id_stage)
        stage = self.hydrate_object_with_json(stage_json)
        return stage

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate tournament object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=s)

    def stage_to_launch(self, stage, list_players):
        stage._status = 1
        self.update_stage_db(stage, stage._id)
        self.stage_view.except_value(f"\nDébut du tours n°{stage._number} :\n")
        # sorted_list_players = self.player_manager.sorted_players(list_players)

    def update_stage_db(self, object_to_update, id_to_object):
        """Update a tournament in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)

