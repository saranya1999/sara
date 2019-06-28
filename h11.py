mod,nod=input().split()
kig={int(k) for kig in input().split()}
vig={int(v) for vig in input().split()}
if vig.issubset(kig):
    print("YES")
else:
    print("NO")
