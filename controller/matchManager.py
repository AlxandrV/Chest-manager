import json

from model.match import Match as m
from controller.databaseManager import DatabaseManager as dbm
from controller.playerManager import PlayerManager as pm
from view.matchView import MatchView as mv

class MatchManager:

    def __init__(self) -> None:
        self.database_manager = dbm()
        self.match_view = mv()
        self.player_manager = pm()
        self.TABLE_NAME = "match"

    def create_match(self, id_stage, match_number, list_two_players):
        """Create a new match"""
        specifiactions = {
            '_number': match_number,
            '_id_stage': id_stage,
            '_id_players': [player._id for player in list_two_players]
        }
        match = m(specifiactions)
        self.database_manager.insert_into_db(self.TABLE_NAME, match)
        return self.database_manager.last_insert(self.TABLE_NAME)

    def close_stage(self, id_stage):
        """Enter the result of match for close a stage in progress"""
        list_match = self.database_manager.search_where(self.TABLE_NAME, "_id_stage", id_stage)
        list_match_object = [self.hydrate_object_with_json(match) for match in list_match]

        for match in list_match_object:
            list_player = []
            for id_player in match._id_players:
                player = self.player_manager.hydrate_object_by_id(id_player)
                list_player.append(player)
            winner = self.match_view.play_match(match, list_player)

            if winner == str(list_player[0]._id):
                list_player[0]._ranking += 1
            elif winner == str(list_player[1]._id):
                list_player[1]._ranking += 1
            elif winner == "nulle":
                list_player[0]._ranking += .5
                list_player[1]._ranking += .5
            
            for player in list_player:
                self.player_manager.update_player_db(player, player._id)
            match._id_winner = winner
            self.update_match_db(match, match._id)

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate match object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=m)

    def update_match_db(self, object_to_update, id_to_object):
        """Update a match in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)
