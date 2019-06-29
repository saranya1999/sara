sak=int(input())
sarr=list(map(int,input().split()[:sak]))
sarm=sorted(sarr)
for i in sarm:
    print(i,end=" ")
