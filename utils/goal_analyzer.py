import re

def indetify_goal(goal: str):
    sports = {
        "cricket"   : ["ipl", "odi", "test", "cricket"],
        "football  ": ["premier league", "la liga", "football"],
        "basketball": ["nba", "basketball"],
        "tennis"    : ["tennis", "atp", "wta"]
    }

    goal = goal.lower()

    for sport, keywords in sports.items():
        for k in keywords:
            if k in goal:
                return sport
            
    return "unknown"