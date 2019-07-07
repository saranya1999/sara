umoa=list(input())
xy=[]
for i in umoa:
 if i not in xy:
  xy.append(i)
if(umoa==xy):
 print("Yes")
else:
 print("No")
