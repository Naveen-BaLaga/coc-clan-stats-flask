from flask import request, jsonify
from helpers.player.player_helpers import *

def route_get_player():
    player_id = request.args.get('player-id')
    
    response = get_player_data(player_id)
    
    return response
    
    