a,b = map(int, input().split())

def my_def(a,b):
    if b > a:
        b += 25
        a *= 2
    else:
        a += 2
        b *= 25
    return a, b
    
result = my_def(a,b)
print(*result)