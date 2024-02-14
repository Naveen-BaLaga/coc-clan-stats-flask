import os
import requests

def get_clan_data(clan_id):
    # Fetch the Authorization Token from the environment variable
    auth_token = os.getenv('AUTH_TOKEN')

    # Check if the AUTH_TOKEN is available
    if not auth_token:
        return {'status': 'Failure', 'data': 'Authorization Token not provided'}

    # URL for the Clash of Clans API
    api_url = f'https://api.clashofclans.com/v1/clans/%23{clan_id}'
    #print(api_url)
    # Set the Authorization header with the token
    headers = {'Authorization': f'Bearer {auth_token}'}

    try:
        # Make the HTTP GET request
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return {'status': 'Success', 'data': response.json()}
        else:
            # If not successful, return the error message
            return {'status': 'Failure', 'data': f'Request failed with status code {response.status_code}'}

    except Exception as e:
        # Handle any exceptions that may occur during the request
        return {'status': 'Failure', 'data': f'Error during request: {str(e)}'}

# Example usage
clan_id = 'your_player_id_here'
#result = get_player_data(clan_id)
#print(result)
