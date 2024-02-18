from flask import Flask
from flask_cors import CORS
from controllers.player.player_controller import route_get_player
from controllers.clans.clans_controller import route_get_clan
app = Flask(__name__)
CORS(app)

@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

@app.route('/')
def hello():
    return "Hello!"

# Route to return the full player data
app.add_url_rule('/get-player', methods=['GET'], view_func=route_get_player)

# Route to return full clan data
app.add_url_rule('/get-clan', methods=['GET'], view_func=route_get_clan)
if __name__ == '__main__':
    app.run()
    