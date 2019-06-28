hug=int(input())
hul=list(map(int,input().split()))
hus=[]
for i in hul:
    if(i==hul.index(i)):
        hus.append(i)
print(*(sorted(hus)))
if(len(hus)==0):
    print(-1)
