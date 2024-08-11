n = int(input())

line = [0] * 200001
black = [0] * 200001
white = [0] * 200001

# 중간 지점으로 시작 위치 설정
cur_idx = 100000

w, b, g = 0, 0, 0
# 흰색 1 / 검정색 2

for _ in range(n):  # n번 입력
    x, dirt = input().split()
    x = int(x)  # 정수형으로 변환

    # 검정
    if dirt == "R":
        for i in range(x):
            line[cur_idx + i] = 2
            black[cur_idx + i] += 1
        cur_idx += x - 1  # 중복된 마지막 위치를 고려하여 이동
    # 하양
    elif dirt == "L":
        for j in range(x):
            line[cur_idx - j] = 1
            white[cur_idx - j] += 1
        cur_idx -= x - 1

# 색상 계산
for k in range(len(line)):
    if black[k] >= 2 and white[k] >= 2:
        g += 1
    elif line[k] == 1:
        w += 1
    elif line[k] == 2:
        b += 1

print(w, b, g)