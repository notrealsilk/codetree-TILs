a, b = map(int,input().split())


def result(a,b):
    num_count = 0
    # 3의 배수
    for i in range(a,b+1):
        if i % 3 == 0 or a_b_compre(i):
            num_count +=1
    return num_count


# 3,6,9
def a_b_compre(i):
    i_list = list(map(int,str(i)))
    for j in i_list:
        if j in [3,6,9]:
            return True

print(result(a,b))