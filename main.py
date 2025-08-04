from mcp.server.fastmcp import FastMCP
from github import Github
import requests, os
from dotenv import load_dotenv
from github.GithubException import GithubException


load_dotenv() 

g = Github(os.getenv("GITHUB_TOKEN")) 
mcp = FastMCP("Github")



@mcp.tool()
def get_user_bio(username: str) -> str:
    """
    Fetch Github user Bio

    Args:
        username(str): The username of the person

    Returns:
        str: User bio
    
    """
    user = g.get_user(username)

    if not user.bio:
        return "No bio available for this user."
    
    return user.bio 



@mcp.tool()
def get_github_files(owner: str, repo: str, path: str) -> dict:
    """
    Recursively fetch all files and directories from a GitHub repo starting at 'path'.
    Returns a dict with directories as nested dicts and files as strings (file paths).


    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        path (str): The path to start fetching files from.
    
    Returns:
        dict: A dictionary representing the file structure of the repository.


    """
    tree = {}
    contents = g.get_repo(f"{owner}/{repo}").get_contents(path)
    
    for content in contents:
        if content.type == "dir":
            tree[content.name] = get_github_files(owner, repo, content.path)
        else:
            tree[content.name] = content.path  # or you can get file content if you want
    
    return tree


@mcp.tool()
def get_file_content(owner: str, repo: str, path: str) -> str:
    """
    Fetches the content of a file from a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        path (str): The path to the file in the repository.

    Returns:
        str: The content of the file.
    """
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return f"Error fetching file: {response.status_code}"
    

@mcp.tool()
def create_pull_request_with_branch(
    repo_name: str,
    base_branch: str,
    new_branch: str,
    pr_title: str,
    pr_body: str = "",
    files_to_commit: dict = None,  # Optional: { "file_path": "file_content" }
    commit_message: str = "Initial commit on new branch"
):
    """
    Creates a new branch and then a pull request on GitHub.

    Parameters:
    - repo_name: e.g., 'user/repo'
    - base_branch: branch to branch off (e.g. 'main')
    - new_branch: name of new branch to create
    - pr_title: title of the PR
    - pr_body: body/description of the PR
    - files_to_commit: optional dict of files to commit { "path": "content" }
    - commit_message: commit message for new changes

    Returns:
    - dict with PR URL or error
    """
    try:
        repo = g.get_repo(repo_name)

        base_ref = repo.get_branch(base_branch)
        base_sha = base_ref.commit.sha

        ref_name = f"refs/heads/{new_branch}"
        repo.create_git_ref(ref=ref_name, sha=base_sha)

        
        if files_to_commit:
            for file_path, content in files_to_commit.items():
                try:
                    repo.create_file(
                        path=file_path,
                        message=commit_message,
                        content=content,
                        branch=new_branch
                    )
                except GithubException as e:
                    return {"success": False, "error": f"File commit failed: {e}"}


        pr = repo.create_pull(
            title=pr_title,
            body=pr_body,
            head=new_branch,
            base=base_branch
        )

        return {"success": True, "url": pr.html_url}

    except GithubException as e:
        return {"success": False, "error": str(e)}




@mcp.tool()
def create_github_issue(
    repo_name: str,
    title: str,
    body: str = "",
    labels: list = None,
    assignees: list = None
):
    """
    Creates an issue on a GitHub repository.
    
    Parameters:

    - repo_name: Full repo name in format "owner/repo".
    - title: Title of the issue.
    - body: Description/body of the issue.
    - labels: List of label names to attach (optional).
    - assignees: List of GitHub usernames to assign the issue to (optional).
    
    Returns:
    - The URL of the created issue or error message.
    """
    try:
        repo = g.get_repo(repo_name)

        issue = repo.create_issue(
            title=title,
            body=body,
            labels=labels if labels else [],
            assignees=assignees if assignees else []
        )

        return {"success": True, "url": issue.html_url}

    except GithubException as e:
        return {"success": False, "error": str(e)}
    


if __name__ == "__main__":
    mcp.run()


