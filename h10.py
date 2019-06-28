j1=int(input())
arr=list(map(int,input().split()))
c=len(arr)
large=max(arr)
g,h=0,0
for i in range(0,c-1):
    for j in range(i+1,c):
        if abs(arr[i]+arr[j])< large:
            g,h=arr[i],arr[j]
            large=abs(g+h)
print(g,h)
