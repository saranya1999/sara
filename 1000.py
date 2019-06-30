nas =int(input())
if(nas>1):
   for i in range(2,nas):
       if (nas % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
