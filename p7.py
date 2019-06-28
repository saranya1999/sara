ash=input()
l=[ash[i] for i in range(len(ash)) if i%2==0]
l1=[ash[i] for i in range(len(ash)) if i%2!=0]
for j in range(len(ash)//2):
  print(l1[j]+l[j],end="")
