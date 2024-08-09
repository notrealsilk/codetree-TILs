n, k, T = map(str,input().split())
word = []
result_word = []

# 단어 입력받고 리스트로 만들기
for i in range(int(n)):
    word.append(input())
    if word[i][:2] == T:
        result_word.append(word[i])

word.sort()
print(word[int(k)])