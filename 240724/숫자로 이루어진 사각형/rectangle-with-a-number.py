def print_rect(N):
    num = 1
    # [] 행
    for i in range(N):
        # [][] 열
        for j in range(N):
            print(num,end = " ")
            num += 1
            # 단, 9다음에는 1이 나와야 함
            if num > 9:
                num = 1
        print() # 두번째 for문이 끝나면 줄바꿈으로 열을 바꿈



N = int(input())
print_rect(N)