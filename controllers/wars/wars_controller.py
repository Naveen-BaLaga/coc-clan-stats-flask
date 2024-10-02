from flask import request, jsonify
from helpers.wars.wars_helpers import *

def route_get_current_war():
    clan_id = request.args.get('clan-id')
    
    response = get_current_war_data(clan_id)
    
    return response