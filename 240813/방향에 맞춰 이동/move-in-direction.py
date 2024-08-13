N = int(input())
x,y = 0,0

for i in range(N):
    dirt, loc = input().split()
    loc = int(loc)
    if dirt == "N":
        y += loc 
    elif dirt == "E":
        x += loc 
    elif dirt == "S":
        y -= loc 
    elif dirt == "W":
        x -= loc 
print(x, y)