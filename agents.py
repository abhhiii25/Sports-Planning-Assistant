from crewai import Agent
from config import get_llm
from tools.stats_tool import fetch_team_data, fetch_league_data

llm = get_llm()


goal_analyzer_agent = Agent(
    role="Sports Goal Analyzer",

    goal="""
Automatically detect sport, league, teams or players from the user goal.
""",

    backstory="""
You are an expert sports knowledge system.

You can detect sports context from short queries like:
- "NBA Lakers stats"
- "IPL match statistics"
- "Messi performance"

Never ask the user questions.
Always infer information from the goal.
""",

    llm=llm,
    verbose=True
)


planner_agent = Agent(
    role="Sports Planning Agent",

    goal="Create an execution plan for sports analysis",

    backstory="""
Expert sports strategist that creates structured plans
to retrieve and analyze sports data.
""",

    llm=llm,
    verbose=True
)


data_agent = Agent(
    role="Sports Data Retrieval Agent",

    goal="""
Retrieve sports information using available tools and decide
which tool to call based on the user's goal.
""",

    backstory="""
    You are an intelligent sports data retrieval system.

    Always follow this format:

    Thought: What information do I need?
    Action: Which tool should I call?
    Action Input: Tool parameters
    Observation: Tool result
    Thought: Decide next step

    Repeat until enough information is gathered.

    Never answer without reasoning.
    """,

    tools=[fetch_team_data, fetch_league_data],

    llm=llm,

    verbose=True,

    allow_delegation=False
)


analysis_agent = Agent(
    role="Sports Data Analyst",

    goal="Analyze sports statistics and generate insights",

    backstory="""
Professional sports data analyst capable of analyzing
team performance and statistics.
""",

    llm=llm,
    verbose=True
)