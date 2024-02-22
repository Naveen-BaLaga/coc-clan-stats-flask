from flask import request, jsonify
from helpers.tables.tables_helpers import *

def route_get_tables():
    table_name = request.args.get('Table Name')
    
    response = get_tables_data(table_name)
    
    return response