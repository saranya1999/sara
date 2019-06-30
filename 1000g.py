nas=int(input())
ga,ak=map(int,input().split())
for i in range(ga,ak+1):
  if(nas==i):
   print("yes")
   break
else:
   print("no")
