import os
import subprocess

def modify_book_toml(remove=True):
    """
    Function to remove or re-add specific lines to book.toml
    """
    book_toml_path = 'book.toml'
    remove_lines_pdf = [
        "[output.pandoc.profile.pdf]",
        "output-file = \"output.pdf\"",
        "to = \"latex\""
    ]
    remove_lines_epub = ["[output.epub]"]

    

    # Read the book.toml file
    with open(book_toml_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Modify the file content based on the operation
    if remove:
        # Remove the specific lines
        lines = [line for line in lines if line.strip() not in remove_lines_pdf + remove_lines_epub]
    else:
        # Re-add the specific lines
        lines.extend([
            "\n[output.pandoc.profile.pdf]\n",
            "output-file = \"output.pdf\"\n",
            "to = \"latex\"\n",
            "\n[output.epub]\n"
        ])

    # Write the modified content back to the file
    with open(book_toml_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def modify_md_files(add=True):
    """
    Function to add or remove a specific line in every .md file except SUMMARY.md
    """
    src_dir = 'src'
    target_line = "[Get PDF](https://makepythonfaster.gumroad.com/l/get)"

    # Traverse through every .md file in 'src' and its subfolders
    for root, _, files in os.walk(src_dir):
        for file_name in files:
            if file_name.endswith('.md') and file_name != 'SUMMARY.md':
                file_path = os.path.join(root, file_name)

                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                if add:
                    # Add the target line if not already present
                    if target_line not in lines:
                        lines.append('\n' + target_line + '\n')
                else:
                    # Remove the target line if present
                    lines = [line for line in lines if line.strip() != target_line]

                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

# Step 1: Remove specific lines from book.toml
modify_book_toml(remove=True)

# Step 2: Change directory to 'src'


# Step 3: Add a line to every .md file in 'src' except 'SUMMARY.md'
modify_md_files(add=True)

# Step 4: Change directory back to the parent


# Step 5: Run 'mdbook build'
subprocess.run(["mdbook", "build"])

# Step 6: Change directory to 'book'
os.chdir('book')

# Step 7: Run 'sscli -b https://makepythonfaster.com'
subprocess.run(["sscli", "-b", "https://makepythonfaster.com"])

# Step 8: Change directory back to the parent
os.chdir('..')

# Step 9: Add changes to git
subprocess.run(["git", "add", "."])

# Step 10: Commit changes with today's date
subprocess.run(["git", "commit", "-m", "updated today"])

# Step 11: Push changes to the repository
subprocess.run(["git", "push"])

# Step 12: Change directory to 'src'


# Step 13: Remove the specific line from every .md file
modify_md_files(add=False)

# Step 14: Change directory back to the parent


# Step 15: Re-add specific lines to book.toml
modify_book_toml(remove=False)

print("All tasks completed successfully.")
