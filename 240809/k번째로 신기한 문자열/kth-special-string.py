n, k, T = map(str,input().split())
word = []

# 단어 입력받고 리스트로 만들기
for i in range(int(n)):
    word.append(input())

word.sort()
print(word[int(k)])