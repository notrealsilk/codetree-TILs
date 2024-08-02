n = int(input())
word = []

for _ in range(n):
    a = input()
    word.append(a)

word.sort()

for i in word:
    print(i)