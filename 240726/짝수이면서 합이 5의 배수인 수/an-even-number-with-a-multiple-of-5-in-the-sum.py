N = int(input())

def result(N):
    # 두 자리를 분리하기 위해 문자열로 타입변환
    N_str = str(N)
    # 인덱싱으로 두 자리 분리, 각각 변수 저징
    n, m = int(N_str[0]), int(N_str[1])
    if N % 2 == 0 and (n+m) % 5 == 0 :
        return 'Yes'
    else :
        return 'No'

print(result(N))