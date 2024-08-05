def modify(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # 짝수
            arr[i] //= 2    # 2로 나눠서 배열 수정




N = int(input())
N_num = list(map(int, input().split()))

modify(N_num)

for element in N_num:
    print(element, end=' ')