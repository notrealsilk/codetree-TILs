n, k, T = map(str,input().split())
word = [input() for i in range(int(n))]
result_word = []


# 단어 입력받고 리스트로 만들기
for i in range(int(n)):
    if word[i][:2] == T:
        result_word.append(word[i])

result_word.sort()
print(result_word[int(k)-1])