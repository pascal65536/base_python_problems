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

steps_dct = {
    "move_up": [1, 0],
    "move_down": [-1, 0],
    "move_right": [0, 1],
    "move_left": [0, -1],
}


def get_mazekey(word):
    maze_str, key_str, *_ = word.split("(")
    key = int(key_str.split(")")[0] or 1)    
    return maze_str.strip(), key


mult = 1
coords = [0, 0]
for word in prg.split("\n"):
    if not word:
        continue
    if word == "# это последняя строка":
        continue
    if ":" in word:
        _, mult = get_mazekey(word)
        continue
    elif word == word.lstrip():
        mult = 1
    maze_str, key = get_mazekey(word)
    maze = steps_dct.get(maze_str)
    for num in range(2):
        coords[num] += maze[num] * mult * key

print(coords)
