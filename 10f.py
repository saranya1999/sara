sok=str(input())
kok=0
ll=0
mom=len(sok)
for i in range(0,mom):
  if sok[i].isalpha():
    kok=kok+1
  if sok[i].isnumeric():
    ll=ll+1
if kok == 0 or ll == 0:
  print("No")
else:
  print("Yes")
