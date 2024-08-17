N = int(input())
arr = [[0]*10 for _ in range(10)]

width = 0

for i in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    # 1로 색칠
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1


for j in range(10):
    for k in range(10):
        if arr[j][k] == 1:
            width +=1
print(width)