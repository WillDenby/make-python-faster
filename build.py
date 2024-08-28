import os
import subprocess
from datetime import datetime

# Step 1: Build the mdbook
subprocess.run(["mdbook", "build"])

# Step 2: Change directory to 'book'
os.chdir("book")

# Step 3: Execute sscli command
subprocess.run(["sscli", "-b", "https://makepythonfaster.com"])

# Step 4: Change directory back to the parent
os.chdir("..")

# Step 5: Add changes to git
subprocess.run(["git", "add", "."])

# Step 6: Commit changes with today's date
today = datetime.today().strftime('%Y-%m-%d')
subprocess.run(["git", "commit", "-m", f"Updated to {today}"])

# Step 7: Push changes to the repository
subprocess.run(["git", "push"])
