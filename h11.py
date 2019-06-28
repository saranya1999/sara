mod,nod=input().split()
kig={int(kig) for kig in input().split()}
vig={int(vig) for vig in input().split()}
if vig.issubset(kig):
    print("YES")
else:
    print("NO")
