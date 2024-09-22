from crewai import Crew,Process
from agents import repo_analyzer, linkedin_writer
from tasks import fetch_repo_task, analyze_repo_task, generate_post_task

# Forming the GitHub to LinkedIn post crew with enhanced configurations
github_to_linkedin_crew = Crew(
    agents=[repo_analyzer, linkedin_writer],
    tasks=[fetch_repo_task, analyze_repo_task, generate_post_task],
    process=Process.sequential,  # Sequential task execution
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)
