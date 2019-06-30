jak=int(input())
jak=str(jak)
fa=0
for i in range(0,len(jak)):
 if(jak[i]=='0' or jak[i]=='1'):
  fa=1
 else:
  fa=0
  break
if(fa==1):
 print('yes')
else:
 print('no')
