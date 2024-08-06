def double(A):
    char = set(A)  # 문자열 중복 없는 집합
    if len(char) >= 2: 
        return "Yes"
    else:
        return "No"

A = input()
print(double(A))