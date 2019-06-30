lba=int(input())
for i in range (1,lba+1):
    if lba % i == 0:
        print(i,end=" ")
