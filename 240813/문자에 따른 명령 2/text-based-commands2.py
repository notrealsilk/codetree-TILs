dirt = list(input())
dir_num = 2
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(len(dirt)):
    if i == "L":
        # 시계
        dir_num = (dir_num + 1) % 4
    elif i == "F":
        # 반시계
        dir_num = (dir_num - 1 + 4) % 4

    nx, ny = x + dx[dir_num], y + dy[dir_num]
print(nx, ny)