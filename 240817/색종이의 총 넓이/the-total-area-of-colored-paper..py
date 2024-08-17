n = int(input())

arr = [[0]*200 for _ in range(200)]

for _ in range(n):
    x,y = map(int,input().split())

    x += 100
    y += 100

    for i in range(x,x+8):
        for j in range(y,y+8):
            arr[i][j] = 1

width = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            width += 1
print(width)