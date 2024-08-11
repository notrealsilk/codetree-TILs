n = int(input())

line = [0]*1001 # 위치 0은 line[500]
black = [0]*1001
white = [0]*1001

cur_idx = 500 # (위치 0) 시작 인덱스

w,b,g = 0,0,0
# 흰색 1 / 검정색 2

area = 0

for _ in range(n): # 4번 입력
    x, dirt = input().split()
    x = int(x) # 정수형으로 바꾸기

# 오른쪽이면 인덱스를 사용해서 오른쪽으로 x번 이동 (검정색)
    if dirt == "R":
        for i in range(x): # x번 반복
            line[cur_idx+i] = 2
            black[cur_idx+i] += 1
        cur_idx += x-1   


# 왼쪽 (흰색)
    elif dirt == "L":
        for j in range(x):
            line[cur_idx-j] = 1
            white[cur_idx-j] += 1
        cur_idx -= x-1



for k in range(len(line)):
    if black[k] >= 2 and white[k] >= 2:
        g += 1
    elif line[k] == 1:
        w += 1
    elif line[k] == 2:
        b += 1

print(w,b,g)