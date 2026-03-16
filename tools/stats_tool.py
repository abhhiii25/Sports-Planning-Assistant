from crewai.tools import tool

try:
    from .sports_api import search_team, search_league
except ImportError:
    from tools.sports_api import search_team, search_league

@tool
def fetch_team_data(team_name: str):

    """
    Use this tool when a team name is mentioned in the goal.

     Example:
    Goal: Analyze Lakers performance
    Tool Call: fetch_team_data("Los Angeles Lakers")
    """

    data = search_team(team_name)

    return str(data)


fetch_team_statistics = fetch_team_data

@tool
def fetch_league_data(league_name: str):
    """
    Fetch league information such as sport type and country.
    Use when a league is mentioned in the goal.
    """

    data = search_league(league_name)

    return str(data)
