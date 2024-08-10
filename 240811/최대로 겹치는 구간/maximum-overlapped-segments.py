n = int(input()) # 선분 갯수 입력

line = [0]*200
max_line = float("-inf")

for i in range(n):
    x1,x2 = map(int,input().split())
    for j in range(x1, x2):
        line[j+100] +=1
    
for k in line:
    if max_line < k:
        max_line = k
print(max_line)