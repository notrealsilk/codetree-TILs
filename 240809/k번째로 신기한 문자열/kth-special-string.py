n, k, T = map(str,input().split())
word = []

# 단어 입력받고 리스트로 만들기
for _ in range(int(n)):
    a = input()
    if a[0:2] == T:
        word.append(a)

word.sort()
print(word[int(k)-1])