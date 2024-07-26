# 최대공약수 구하는 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 구하는 함수
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

n, m = map(int, input().split())

# 100 이하의 최소공배수를 찾기
result = lcm(n, m)
print(result)

'''
n, m = map(int, input().split())

i = 1
while i <= 100:
    if i % n ==0 and i % m ==0 :
        result = i
        break
    i += 1
print(result)
'''