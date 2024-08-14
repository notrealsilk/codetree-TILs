n, k = map(int,input().split())
arr = list(map(int,input().split()))

max_sum = 0
for i in range(n - k + 1):
    max_val = 0
    for j in range(i, i + k):
        max_val += arr[j]

    if max_sum < max_val:
        max_sum = max_val

print(max_sum)