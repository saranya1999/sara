nu=int(input())
mk=0
i=0
while nu > 0:
  i=nu%10
  nu=nu//10
  mk=mk+i
print(mk)
