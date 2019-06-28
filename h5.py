non=int(input())
aopa=list(map(int,input().split()))
bop=[]
for i in aopa:
  if(aopa.count(i)>1):
    bop.append(i)
  else:
    print(i)
