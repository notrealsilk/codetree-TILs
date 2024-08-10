# 1. 입력, 사전작업
# N: 가로 칸수, K : 쌓는 횟수
N, K = map(int,input().split())

# N 크기만큼 리스트 할당
# [0]은 무시
N_list = [0]*(N+1) 
max_result = float("-inf")

# 2. 반복문과 입력받기
# 범위는 쌓는횟수 순회
for i in range(1, K+1):
    ai,bi = map(int,input().split())
    for j in range(ai,bi+1):
        N_list[j]+=1

for j in N_list:
    if max_result < j:
        max_result = j
print(max_result)