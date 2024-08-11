N = int(input()) # 색 바꾸는 횟수

# 초기 설정
color = [0]*200001
# whiht = [0]*200001
# black = [0]*200001

# 음수 인덱스가 있을 수 있으므로 시작을 중간으로
color_idx = 100000

w, b = 0, 0

# 흰색 1 / 검정 2

for n in range(N):
    x, dirt = input().split()
    x = int(x) # 정수형으로 바꾸기

    # 흰색 / 왼쪽 / 1
    if dirt == "L":
        # color_idx ~ color_idx+x 인덱스를 색칠
        for i in range(x):
            color[color_idx-i] = 1
        color_idx -= x - 1


    # 검정 / 오른쪽 / 2
    if dirt == "R":
        for i in range(x):
            color[color_idx+i] = 2
        color_idx += x - 1

# 갯수 카운트
for j in color:
    if j == 1:
        w+=1
    elif j == 2:
        b+=1

print(w, b)