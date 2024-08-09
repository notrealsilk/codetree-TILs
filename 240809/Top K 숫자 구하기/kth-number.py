n, k = map(int, input().split())
a = list(map(int,input().split()))
a.sort()

for i in range(n):
    if i == k-1:
        b = i
        break
print(a[b])