N = int(input())

# 200x200 배열 생성 (모든 좌표를 커버하기 위해 0~199로 구성)
arr = [[0] * 200 for _ in range(200)]

width = 0

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 좌표를 0 ~ 199 범위로 맞추기 위해 100을 더함
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    
    # 1로 색칠
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1

# 넓이 계산
for j in range(200):
    for k in range(200):
        if arr[j][k] == 1:
            width += 1

print(width)