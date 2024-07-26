n, m = map(int, input().split())

i = 1
while i <= 100:
    if i % n ==0 and i % m ==0 :
        result = i
        break
    i += 1
print(result)