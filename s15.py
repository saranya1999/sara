nu=input()
xnx=0
for i in range(len(nu)):
  if(nu[i].isdigit() or nu[i].isalpha() or nu[i]==(' ')):
    continue
  else:
    xnx+=1
print(xnx)
