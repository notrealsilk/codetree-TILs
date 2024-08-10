n = int(input())

line = [0]*101 # 인덱스 0은 무시

for i in range(n):
    x1, x2 = map(int,input().split())
    for j in range(x1, x2+1):# 끝 점도 겹치는 것으로 포함
        line[j] += 1

print(max(line))