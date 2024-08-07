a = list(map(str,input()))
b = list(map(str,input()))

for i in a :
    if i in b :
        b.remove(i)

# for문이 끝났을 때 b가 비어있으면 a,b는 동일한 알파벳 ㅇ
if b == []:
    print("Yes")
else :
    print("No")