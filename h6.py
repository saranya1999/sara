number=input()
f=1
for i in range(len(number)-1):
    sos=number[i]+number[i+1]
    p=int(sos)
    if p<=26 and number[i]!="0":
        f+=1
if f==3:
    print(f)
else:
    print(f+(f-1)//2
