import os


graph = []
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for x in f.readlines():
        graph.append(x.strip())

h = len(graph)
w = len(graph[0])

p1 = 0
p2 = 0


def get_words_in_directions(graph, r, c, max_len=4):
    rows = len(graph)
    cols = len(graph[0])

    # Define the 8 directions as row and column offsets
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    # Function to check if the indices are within bounds
    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Get letters up to 4 letters long in all 8 directions
    results = {}
    for dr, dc in directions:
        word = ""
        for i in range(0, max_len):
            nr, nc = r + i * dr, c + i * dc
            if in_bounds(nr, nc):
                word += graph[nr][nc]
            else:
                break
        # Store the result for this direction
        results[(dr, dc)] = word

    return results


def check_diagonal_words(graph, r, c):
    """
    Extract two diagonal words starting from the central letter at (r, c).
    - Diagonal 1: (-1, -1), (0, 0), (1, 1)
    - Diagonal 2: (-1, 1), (0, 0), (1, -1)
    """
    rows = len(graph)
    cols = len(graph[0])

    # Helper function to check bounds
    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Extract first diagonal (-1, -1), (0,0), (1, 1)
    word1 = ""
    for i in range(-1, 2):  # indices -1, 0, 1
        nr, nc = r + i, c + i
        if in_bounds(nr, nc):
            word1 += graph[nr][nc]
        else:
            break

    # Extract second diagonal (-1, 1), (0, 0), (1, -1)
    word2 = ""
    for i in range(-1, 2):  # indices -1, 0, 1
        nr, nc = r + i, c - i
        if in_bounds(nr, nc):
            word2 += graph[nr][nc]
        else:
            break

    return word1, word2


for r in range(0, h):
    for c in range(0, w):
        if graph[r][c] == "X":
            p1 += [
                value for _, value in get_words_in_directions(graph, r, c, 4).items()
            ].count("XMAS")
        if graph[r][c] == "A":
            word_count = check_diagonal_words(graph, r, c)
            if word_count.count("MAS") + word_count.count("SAM") == 2:
                p2 += 1

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")