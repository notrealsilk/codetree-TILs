def modify(string):
    for i in range(len(string)):
        # 순회하는 동안 대칭 문자열이 같지 않으면
        # 회문이 아니므로 No 반환
        if string[i] != string[len(string)-i-1]:
            return "No" 
    # 순회를 끝냈다 = 문자열들이 대칭이다.
    return "Yes"



word = input()
print(modify(word))