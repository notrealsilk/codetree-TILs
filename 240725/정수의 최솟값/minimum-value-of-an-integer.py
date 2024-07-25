def min_nums(a,b,c):
    min_num = a

    nums = []
    nums.append(b)
    nums.append(c)

    for i in nums:
        if i < min_num :
            min_num = i
    return min_num


a,b,c = map(int, input().split())
print(min_nums(a,b,c))