arr = [[0]*2000 for _ in range(2000)]

# A,B 색칠
for _ in range(2):
    x1,y1,x2,y2 = map(int,input().split())

    x1 += 1000
    x2 += 1000
    y1 += 1000
    y2 += 1000

    for i in range(x1,x2):
        for j in range(y1, y2):
            arr[i][j] = 1

# M 색칠
x1,y1,x2,y2 = map(int,input().split())

x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1,x2):
    for j in range(y1, y2):
            arr[i][j] = 2

width = 0
for i in range(2000):
    for j in range(2000):
        if arr[i][j] == 1:
            width += 1
print(width)