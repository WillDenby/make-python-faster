import os
import subprocess
from datetime import datetime
import shutil
import glob


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


# Step 8: Copy the 'src' directory to 'pdf'
src_dir = 'src'
dst_dir = 'pdf'
shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)  # 'dirs_exist_ok=True' allows overwriting if 'pdf' already exists

# Step 9: Change directory to 'pdf'
os.chdir(dst_dir)

# Step 10: Traverse through every .md file in 'pdf' and its subfolders
md_files = glob.glob('**/*.md', recursive=True)

# Step 11: Remove the last line if it matches the specific text
remove_line = "[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)"

for md_file in md_files:
    # Read the content of the file
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Check and remove the last line if it matches
    if lines and lines[-1].strip() == remove_line:
        lines = lines[:-1]  # Remove the last line
    
    # Write the modified content back to the file
    with open(md_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

print("Completed processing all .md files in the 'pdf' directory.")
