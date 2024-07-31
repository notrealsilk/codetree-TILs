def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def mul(a, c):
    return a * c

def div(a, c):
    return int(a / c)

a, o, c = input().split()

# 숫자형 변환
a = int(a)
c = int(c)


if o == '+':
    result = plus(a, c)
elif o == '-':
    result = minus(a, c)
elif o == '*':
    result = mul(a, c)
elif o == '/':
    result = div(a, c)
else:
    result = 'False'

print(f"{a} {o} {c} = {result}")