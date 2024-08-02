n = int(input()) # n개 원소
nums = list(map(int,input().split()))

nums.sort()
for i in nums:
    print(i, end = " ")
print()    
nums.sort(reverse = True)
for i in nums:
    print(i, end = " ")