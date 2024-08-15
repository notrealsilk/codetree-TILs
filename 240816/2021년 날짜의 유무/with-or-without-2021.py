def Day(M,D):

    if M in [1,3,5,7,8,10,12]:
        if D <= 31:
            return "Yes"
    elif M in [4,6,9,11]:
        if D <= 30:
            return "Yes"
    else:
        if D <= 28:
            return "Yes"
    return "No"


# M: 월 /D: 일
M,D = map(int,input().split())

print(Day(M,D))