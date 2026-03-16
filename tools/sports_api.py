import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("SPORTS_API")

def search_team(team_name):

    url = f"{BASE_URL}/searchteams.php"

    params = {"t": team_name}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    return None

def search_league(league_name):
    url = f"{BASE_URL}/search_all_leagues.php"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        leagues = data.get("leagues", [])

        for league in leagues:
            if league_name.lower() in league["strLeague"].lower():
                return league
            
    else:
        return None
    
def search_players(player_name):

    url = f"{BASE_URL}/searchplayers.php"

    params = {"p": player_name}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    return None