N = int(input())
list1 = list(map(int,input().split())).sort()
list2 = list(map(int,input().split())).sort()

if list1 == list2 :
    print("Yes")

else :
    print("No")