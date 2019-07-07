sbk1=int(input())
sbnt1=list(map(int,input().split()))
for p in range(len(sbnt1)-1):
     if(sbnt1[p]>sbnt1[p+1]):
           print(p)
           break
