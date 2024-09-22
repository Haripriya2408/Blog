from crewai_tools import GithubSearchTool
import os
# Initialize the tool with a specific Youtube channel handle to target your search
github_tool=GithubSearchTool(
    gh_token=os.getenv('GITHUB_ACCESS_TOKEN'),
    content_types=[],  # Replace with valid content types
    repository_url="https://github.com/Haripriya2408/terraform_aws"  # Add the repository URL if needed
)
