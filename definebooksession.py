import requests
import json

def book_session(name, email, date_time):
    # Enter your Zoom API key and secret here
    api_key = 'api_key'
    api_secret = 'api_secret'

    
    # Set up the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_access_token(api_key, api_secret)
    }
    
    # Set up the request body with the meeting details
    data = {
        'topic': 'Cloud Technology Session',
        'type': 2, # Scheduled meeting
        'start_time': '03/10/2023_09:00am', # Meeting start time in UTC format
        'duration': 60, # Meeting duration in minutes
        'timezone': 'UTC',
        'agenda': 'Session with ' + 'Abiola',
        'settings': {
            'host_video': True,
            'participant_video': True,
            'join_before_host': False,
            'mute_upon_entry': False,
            'auto_recording': 'none',
            'waiting_room': False
        }
    }
    
    # Make the API call to create the meeting
    response = requests.post('https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(data))
    
    # Parse the response and get the join URL
    response_data = json.loads(response.text)
    join_url = response_data['join_url']
    
    return join_url


def get_access_token(api_key, api_secret
):
    # Set up the request headers and body to get the access token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': 'api_key',
        'client_secret': 'api_secret'
    }
    
    # Make the API call to get the access token
    response = requests.post('https://zoom.us/oauth/token', headers=headers, data=data)
    
    # Parse the response and get the access token
    response_data = json.loads(response.text)
    access_token = response_data['access_token']
    
    return access_token
