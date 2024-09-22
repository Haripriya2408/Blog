from crewai import Agent
from tools import github_tool


## Create a senior blog content researcher

repo_analyzer=Agent(
    role='GitHub Repository Analyzer',
    goal='Analyze the GitHub repository to extract project aim, workflow, tools, technologies, and functionality.',
    verbose=True,
    memory=True,
    backstory=(
       "An expert in software project analysis, adept at understanding repository structures, "
        "extracting key information about project aims, workflows, tools, technologies, and functionalities."
    ),
    tools=[github_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

linkedin_writer = Agent(
    role='LinkedIn Post Writer',
    goal='Create a professional and engaging LinkedIn post based on the analyzed GitHub repository details.',
    verbose=True,
    memory=True,
    backstory=(
        "A skilled content creator with a knack for transforming technical project details into "
        "compelling and engaging LinkedIn posts that resonate with a professional audience."
    ),
    tools=[],  # No specific tools needed unless integrating with LinkedIn API
    allow_delegation=False
)