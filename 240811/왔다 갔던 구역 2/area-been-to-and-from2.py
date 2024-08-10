n = int(input())

line = [0]*200 # 위치 0은 line[100]
cur_idx = 100 # 위치 0 인덱스

area = 0

for _ in range(n): # 6번 입력
    x, dirt = input().split()
    x = int(x) # 정수형으로 바꾸기

# 오른쪽이면 인덱스를 사용해서 오른쪽으로 x번 이동
    if dirt == "R":
        for i in range(x): # x번 반복
            line[cur_idx+i] += 1
        cur_idx += x

    elif dirt == "L":
        for j in range(x,-1,-1):
            line[cur_idx+j] += 1
        cur_idx -= x


for k in line:
    if k >=2:
        area +=1
print(area)