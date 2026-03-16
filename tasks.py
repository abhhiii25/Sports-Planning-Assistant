from crewai import Task
from agents import goal_analyzer_agent, planner_agent, data_agent, analysis_agent 


goal_analysis_task = Task(
    description="""
    You are given the user's sports goal:{goal}
    
    Your task:

    1. Identify the sport mentioned.
    2. Identify the league if present.
    3. Identify teams or players.
    4. Identify the type of statistics requested.

    Rules:
    - Do NOT ask the user questions.
    - Infer missing information from context.
    - If league is mentioned (NBA, IPL, Premier League etc.) detect the sport automatically.

    Return output in this format:

    Sport:
    League:
    Team/Player:
    Requested Stats:
    """,
    expected_output="""
    A structured summary containing:
    - Sport
    - League
    - Teams or players mentioned
    - Type of statistics requested
    """,
    agent=goal_analyzer_agent
)

planning_task = Task(
    description = """
    Using the extracted sports information, create a step-by-step execution plan.

    User Goal:
    {goal}

    Steps must include:

    1. Sport detection
    2. League verification
    3. Data retrieval
    4. Statistics analysis
    5. Final insights

    Return a structured plan.
    """,
    expected_output=""" A detailed plan with steps to achieve the user's sports goal, including any data or statistics needed.""",
    agent=planner_agent
)

data_task = Task(
    description="""
    Using the detected team or league from the goal:

    {goal}

   Use the following reasoning process:

    1. Identify if a team or league exists in the goal
    2. If a league exists → call fetch_league_data
    3. If a team exists → call fetch_team_data

    Follow ReAct reasoning:

    Thought → Action → Observation → Thought

    Do NOT skip reasoning.
    """,
    expected_output=""" Real-time team statistics and data.""",
    agent=data_agent
)

analysis_task = Task(
    description="""
    Analyze the sports data retrieved.

    User goal:
    {goal}

    Return insights in the format:

    ### Sport
    ### League
    ### Team

    ### Key Statistics
    ### Performance Insights
    ### Summary
    """,
    expected_output=""" Insights and analysis based on the sports data.""",
    agent=analysis_agent
)
