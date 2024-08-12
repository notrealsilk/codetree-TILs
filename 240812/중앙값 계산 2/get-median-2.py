n = int(input())
n_list = list(map(int,input().split()))
#n_list.sort()
result = []
cur_list = []

for i in range(1, len(n_list)+1):
    cur_list.append(n_list[i-1])
    if i % 2 == 1: # 인덱스 홀수
        cur_list.sort()
         # 지금까지 모인 값 중의 인덱스 중앙의 값을 저장
        result.append(cur_list[len(cur_list)//2])
        
print(*result)