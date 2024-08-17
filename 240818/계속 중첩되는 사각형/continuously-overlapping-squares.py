n = int(input())
arr = [[0]*201 for _ in range(201)]

area = 0

for c in range(n):
    x1,y1,x2,y2 = map(int,input().split())

    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    for i in range(x1,x2):
        for j in range(y1,y2):
            if c % 2 == 0: # 빨강색
                arr[i][j] = 1
            elif c % 2 == 1 : # 파란색
                arr[i][j] = 2

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 2 :
            area += 1
print(area)