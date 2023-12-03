import os

# Get user input for year, day, and puzzle
year = input("Enter the year: ")
day = input("Enter the day: ")

# Create the folder structure
folder_path = f"year{year}/day{day}"
os.makedirs(folder_path, exist_ok=True)

# Create the files
answer_file = os.path.join(folder_path, "answer.py")
input_file = os.path.join(folder_path, "input.txt")
puzzle_file_1 = os.path.join(folder_path, "puzzle1.md")
puzzle_file_2 = os.path.join(folder_path, "puzzle2.md")

# Create the answer.py file
with open(answer_file, "w") as file:
    file.write('import os\n\n')
    file.write('with open(f"{os.path.dirname(__file__)}/input.txt") as f:')

# Create the input.txt file
with open(input_file, "w") as file:
    file.write("# Add your input here")

# Create the puzzle1.md file
with open(puzzle_file_1, "w") as file:
    file.write("# Add the puzzle description here")

# Create the puzzle2.md file
with open(puzzle_file_2, "w") as file:
    file.write("# Add the second puzzle description here")
