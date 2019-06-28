ass,ash=map(str,input().split())
if(len(ass)!=len(ass)):
  print("no")
c=[ass.count(i) for i in ass]
d=[ash.count(i) for i in ash]
if c==d:
  print("yes")
else:
  print("no")
