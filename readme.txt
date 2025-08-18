1. script1.sh : Auto-upload modified Files on a Github repository
As a developer, we use Git/Github for literally every project we have. For all the changes, we have to follow a fix set of steps to push our files to Github remote repo.
This process involves multiple manual steps: initializing Git, adding files, committing changes, setting the remote URL, and pushing to GitHub.
This script automates the hassle for you. It takes two arguments, the local folder path and the Github remote repository.
It initializes a git repo is needed, does git add, commit, add remote origin and finally push to main branch.


2. script2.sh : Timestamp backup of any file
We often need to modify the code/files which are working correctly, so its a good practice to copy the same into a backup file, and then do the modifications.
This script creates a timestamped backup of any file provided in the input. The backup filename includes the date and time, making it easy to keep multiple versions and track changes over time.
Command to run : ./script2.sh /path/to/your/file

3. script3.sh : List large files in the system
Over time, a user's home directory can accumulate large files (e.g., videos, backups, log files) that consume significant disk space. Manually searching for these files can be tedious.
This script scans the home directory (~) and lists all files larger than 100 MB, along with their sizes and details(ls -lh).
Command to run : ./script1.sh

4. script4.sh : Clean the Trash folder
We deal with large amount of files on a daily basis, which means frequent file deletions. The deleted files are dumped into Trash folder, and resides until we dont clean up the trash.
This script just do the exact thing, !cleans up the Trash folder!.
Command to run : ./script4.sh