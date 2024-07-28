def year(n):
    if n % 4 == 0:
        return "true"
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    else :
        return "false"

n = int(input())
print(year(n))