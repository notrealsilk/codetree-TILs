x, y = 0, 0
dir_num = 3 #북쪽

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_input = input()

for cdir in dir_input:
    if cdir == 'L':
        dir_num = (dir_num - 1) % 4  # 왼쪽으로 90도 회전
    elif cdir == 'R':
        dir_num = (dir_num + 1) % 4  # 오른쪽으로 90도 회전
    else:
        x += dx[dir_num]  # x축 방향으로 한 칸 이동
        y += dy[dir_num]  # y축 방향으로 한 칸 이동

print(x, y)