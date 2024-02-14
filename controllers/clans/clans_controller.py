from flask import request, jsonify
from helpers.clans.clans_helpers import *

def route_get_clan():
    clan_id = request.args.get('clan-id')
    
    response = get_clan_data(clan_id)
    
    return response