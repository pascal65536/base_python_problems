prg = """
move_right() 
move_right() 
move_right() 
move_down() 
for k in range(8): 
    move_up() 
move_left() 
for k in range(3): 
    move_left() 
move_down() 
for k in range(2): 
    move_down() 
move_right() 
# это последняя строка
"""


def get_mazekey(word):
    steps_dct = {
        "move_up": [1, 0],
        "move_down": [-1, 0],
        "move_right": [0, 1],
        "move_left": [0, -1],
    }
    maze_str, key_str, *_ = word.split("(")
    maze = steps_dct.get(maze_str.strip())
    key = int(key_str.split(")")[0] or 1)
    return maze, key


mult = 1
coords = [0, 0]
for word in prg.split("\n"):
    if not word or word == "# это последняя строка":
        continue
    if ":" in word:
        _, mult = get_mazekey(word)
        continue
    elif word == word.lstrip():
        mult = 1
    maze, key = get_mazekey(word)
    for num in range(2):
        coords[num] += maze[num] * mult * key

print(coords)
