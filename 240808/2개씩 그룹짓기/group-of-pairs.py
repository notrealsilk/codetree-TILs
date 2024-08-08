N = int(input())
nums = list(map(int, input().split()))
nums.sort() 


result = []
for i in range(N):
    a = nums[i]
    b = nums[-(i + 1)] 
    result.append([a, b])

max_sum = max(sum(group) for group in result)
print(max_sum)