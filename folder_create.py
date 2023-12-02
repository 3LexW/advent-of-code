import os

# Get user input for year, day, and puzzle
year = input("Enter the year: ")
day = input("Enter the day: ")
puzzle = input("Enter the puzzle number: ")

# Create the folder structure
folder_path = f"year{year}/day{day}/puzzle{puzzle}"
os.makedirs(folder_path, exist_ok=True)

# Create the files
answer_file = os.path.join(folder_path, "answer.py")
input_file = os.path.join(folder_path, "input.txt")
puzzle_file = os.path.join(folder_path, "puzzle.md")

# Create the answer.py file
with open(answer_file, "w") as file:
    file.write("# Add your solution here")

# Create the input.txt file
with open(input_file, "w") as file:
    file.write("# Add your input here")

# Create the puzzle.md file
with open(puzzle_file, "w") as file:
    file.write("# Add the puzzle description here")
