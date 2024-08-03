N = int(input())

list1 = sorted(map(int, input().split()))
list2 = sorted(map(int, input().split()))

if list1 == list2:
    print("Yes")
else:
    print("No")