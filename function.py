import os
from init import *

def save(research, outline, essay, outcome, name):
    # Check if the folder exists, and create it if it doesn't
    folder_path = output_path + "/" + name
    if os.path.exists(folder_path):
        # Find the next available folder name
        i = 2
        while True:
            folder_path = output_path + "/" + f"{name}_{i}"
            if not os.path.exists(folder_path):
                break
            i += 1

    # Save the research as .txt file
    research_file_name = f"research_{name}.txt"
    if os.path.exists(os.path.join(folder_path, research_file_name)):
        # Find the next available file name
        i = 2
        while True:
            research_file_name = f"research_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, research_file_name)):
                break
            i += 1
    research_file_path = os.path.join(folder_path, research_file_name)
    with open(research_file_path, "w") as research_file:
        research_file.write(research)

    # Save the outline as .txt file
    outline_file_name = f"outline_{name}.txt"
    if os.path.exists(os.path.join(folder_path, outline_file_name)):
        # Find the next available file name
        i = 2
        while True:
            outline_file_name = f"outline_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, outline_file_name)):
                break
            i += 1
    outline_file_path = os.path.join(folder_path, outline_file_name)
    with open(outline_file_path, "w") as outline_file:
        outline_file.write(outline)

    # Save the essay as .txt file
    essay_file_name = f"essay_{name}.txt"
    if os.path.exists(os.path.join(folder_path, essay_file_name)):
        # Find the next available file name
        i = 2
        while True:
            essay_file_name = f"essay_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, essay_file_name)):
                break
            i += 1
    essay_file_path = os.path.join(folder_path, essay_file_name)
    with open(essay_file_path, "w") as essay_file:
        essay_file.write(essay)

    # Save the outcome as .txt file
    outcome_file_name = f"outcome_{name}.txt"
    if os.path.exists(os.path.join(folder_path, outcome_file_name)):
        # Find the next available file name
        i = 2
        while True:
            outcome_file_name = f"outcome_{name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, outcome_file_name)):
                break
            i += 1
    outcome_file_path = os.path.join(folder_path, outcome_file_name)
    with open(outcome_file_path, "w") as outcome_file:
        outcome_file.write(outcome)