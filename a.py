pxq=int(input())
xs=int(pxq/2)
q=0
for i in range (2,xs+1):
    if pxq % i == 0:
        q=1
        print("yes")
        break
if q == 0:
    print("no")
