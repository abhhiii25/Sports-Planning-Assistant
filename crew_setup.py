from crewai import Crew
from agents import goal_analyzer_agent,planner_agent, data_agent, analysis_agent
from tasks import goal_analysis_task,planning_task, data_task, analysis_task


crew = Crew(

    agents=[
        goal_analyzer_agent,
        planner_agent,
        data_agent,
        analysis_agent
    ],

    tasks=[
        goal_analysis_task,
        planning_task,
        data_task,
        analysis_task
    ],

    verbose=True,
    process="sequential",
    tracing=True
)