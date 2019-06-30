la=[int(i) for i in input().split()]
n=la[0]
k=la[1]
la=[int(i) for i in input().split()]
c=0
for i in la:
    if(i==k):
        c=c+1
print(c)
