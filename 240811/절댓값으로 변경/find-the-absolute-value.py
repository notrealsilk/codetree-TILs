N = int(input())
Ns = list(map(float,input().split()))
Ns_list = []

def func(N,Ns):
    for i in range(N):
        Ns_list.append(abs(Ns[i]))

func(N,Ns)

for i in Ns_list:    
   print(int(i), end = " ")