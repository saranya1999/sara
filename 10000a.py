gas=list(input())
if len(gas)%2==0:
    gas[int(len(gas)/2)] ='*'
    gas[int(len(gas)/2)-1]='*'
else:
    gas[int(len(gas)/2)] ='*'
for i in range(0,len(gas)):
    print(gas[i],end='')
