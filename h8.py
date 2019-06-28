noj=int(input())
lo1e=list(map(int,input().split()))
for i1 in range(0,len(lo1e)):
    if(lo1e[i1]%2==0 and i1%2!=0):
            print(lo1e[i1],end=" ")
    elif(lo1e[i1]%2!=0 and i1%2==0):
            print(lo1e[i1],end=" ")
