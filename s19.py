numt=int(input())
fiboo,ga=0,1
print(ga,end=" ")
for i in range(1,numt):
  yy=fiboo+ga
  print(yy,end=" ")
  fiboo,ga=ga,yy
