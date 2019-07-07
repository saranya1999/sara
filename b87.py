sb3,bu4=map(int,input().split())
m=1
while(m<=sb3 and m<=bu4):
 if(sb3%m==0 and bu4%m==0):
  gcd1=m
 m=m+1
print(gcd1)
