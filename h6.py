number=input()
k=1
for i in range(len(number)-1):
    sos=number[i]+number[i+1]
    p=int(sos)
    if p<=26 and number[i]!="0":
        k+=1
if k==3:
    print(k)
else:
    print(k+(k-1)//2
