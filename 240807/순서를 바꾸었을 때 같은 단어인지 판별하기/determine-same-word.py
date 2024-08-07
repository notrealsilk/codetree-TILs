a = list(map(str,input()))
b = list(map(str,input()))

def word(a,b):
    if len(a) != len(b): # 문자열 길이가 다니면 아예 x
        return "No"

    for i in a :
        if i in b :
            b.remove(i)

    # for문이 끝났을 때 b가 비어있으면 a,b는 동일한 알파벳 ㅇ
    if b == []:
        return "Yes"
    else :
        return "No"

print(word(a,b))