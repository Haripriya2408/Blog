# tasks.py

from crewai import Task
from tools import github_tool
from agents import repo_analyzer, linkedin_writer

# Task to fetch repository contents
fetch_repo_task = Task(
    description=(
        "Fetch and retrieve all necessary data from the GitHub repository at {repo_url}."
    ),
    expected_output='A comprehensive collection of repository files and metadata.',
    tools=[github_tool],
    agent=repo_analyzer,
)

# Task to analyze repository
analyze_repo_task = Task(
    description=(
        "Analyze the fetched repository data to extract the project aim, workflow, tools, technologies, and functionality."
    ),
    expected_output='A structured report detailing the project aim, workflow, tools, technologies, and functionality.',
    tools=[],  # Analysis handled by the repo_analyzer agent
    agent=repo_analyzer,
    dependencies=["Fetch Repository"]
)

# Task to generate LinkedIn post
generate_post_task = Task(
    description=(
        "Generate a professional and engaging LinkedIn post based on the analyzed repository details without revealing the actual code."
    ),
    expected_output='A well-formatted LinkedIn post ready for publication.',
    tools=[],  # Using OpenAI directly within the agent
    agent=linkedin_writer,
    dependencies=["Analyze Repository"],
    async_execution=False,
    output_file='linkedin_post.md'  # Example of output customization
)
