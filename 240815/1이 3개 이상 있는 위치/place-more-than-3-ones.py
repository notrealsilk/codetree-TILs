N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0 # 최종결과

for y in range(N):
    for x in range(N):
        cur_cnt = 0
        # 델타 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                cur_cnt += arr[ny][nx]
        if cur_cnt >=3:
            cnt +=1
print(cnt)