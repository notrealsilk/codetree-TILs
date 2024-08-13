dirt = input()
dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in dirt:
    if i == "L":
        dir_num = (dir_num - 1) % 4
    elif i == "F":
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)