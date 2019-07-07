ge11s,se11s=map(int,input().split())
maxima=max(ge11s,se11s)
while(1):
 if(maxima%ge11s==0 and maxima%se11s==0):
  print(maxima)
  break
 maxima+=1
