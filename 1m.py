las=int(input())
b=[]
for i in range(0,las):
    inpu=input()
    b.append(inpu)
lai=[]
for i in zip(*b):
    if(i.count(i[0])==len(i)):
        lai.append(i[0])
            
    else:
        break
print(''.join(lai))
