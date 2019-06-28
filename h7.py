fk=int(input())
gist1=gist(map(int,input().split()))
for i in gist1:
    if(gist1.count(i)>1):
        print(i)
        break
else:
    print("unique")
