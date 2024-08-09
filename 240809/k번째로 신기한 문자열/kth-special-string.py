n, k, T = map(str,input().split())
word = []

# 단어 입력받고 리스트로 만들기
for _ in range(int(n)):
    a = input()
    if a.startswith(T): # 문자열 길이 관계없이 접두사 확인
        word.append(a)

word.sort()
print(word[int(k)-1])