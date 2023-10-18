```python
import os
import subprocess

def initialize_git():
    """
    This function initializes a new Git repository in the current directory.
    """
    subprocess.run(["git", "init"])

def create_new_branch(branch_name):
    """
    This function creates a new branch with the given name.
    """
    subprocess.run(["git", "checkout", "-b", branch_name])

def commit_changes(commit_message):
    """
    This function commits the current changes with the given commit message.
    """
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])

def push_changes(branch_name):
    """
    This function pushes the changes of the given branch to the remote repository.
    """
    subprocess.run(["git", "push", "origin", branch_name])

def pull_changes(branch_name):
    """
    This function pulls the latest changes from the given branch of the remote repository.
    """
    subprocess.run(["git", "pull", "origin", branch_name])

def switch_branch(branch_name):
    """
    This function switches to the given branch.
    """
    subprocess.run(["git", "checkout", branch_name])

def merge_branches(source_branch, target_branch):
    """
    This function merges the source branch into the target branch.
    """
    switch_branch(target_branch)
    subprocess.run(["git", "merge", source_branch])

def view_commit_history():
    """
    This function displays the commit history.
    """
    subprocess.run(["git", "log"])
```