# main.py

from crew import github_to_linkedin_crew
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"

if __name__ == "__main__":
    # Define the GitHub repository URL you want to analyze
    repo_url = "https://github.com/Haripriya2408/terraform_aws"

    # Start the crew execution process with enhanced feedback
    result = github_to_linkedin_crew.kickoff(inputs={'repo_url': repo_url})
    
    # Output the generated LinkedIn post
# main.py

from crew import github_to_linkedin_crew
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"

if __name__ == "__main__":
    # Define the GitHub repository URL you want to analyze
    repo_url = "https://github.com/Haripriya2408/terraform_aws"

    # Start the crew execution process with enhanced feedback
    result = github_to_linkedin_crew.kickoff(inputs={'repo_url': repo_url})
    
    # Output the generated LinkedIn post

    print(result)

