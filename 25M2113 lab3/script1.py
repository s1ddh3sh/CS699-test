import os
import sys
from git import GitCommandError, NoSuchPathError, InvalidGitRepositoryError
from git.repo import Repo

def main():
    folder_path = input("Enter the path to the folder: ").strip()
    remote_url = input("Enter the GitHub remote URL: ").strip()

    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        sys.exit(1)

    try:
        repo = Repo(folder_path)
    except(InvalidGitRepositoryError, NoSuchPathError):
        print("Initializing new Git repository...")
        repo = Repo.init(folder_path)
    
    try:
        repo.git.add(A=True)
        if repo.is_dirty(untracked_files=True):
            commit_message = input("Enter your commit message: ").strip()
            repo.index.commit(commit_message)
        else:
            print("No changes to commit.")

         # Set branch to main (if not already)
        try:
            repo.git.branch('-M', 'main')
        except GitCommandError:
            pass  # Might already be on main

        if "origin" not in [remote.name for remote in repo.remotes]:
            repo.create_remote("origin",remote_url)

        # Push to remote
        print("Pushing to GitHub...")
        repo.git.push("--set-upstream", "origin", "main")
        print(f"✅ Latest changes uploaded to GitHub repo: {remote_url}")
    except GitCommandError as e:
        print(f"Git error : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()