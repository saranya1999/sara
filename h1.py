
s = int(input())
o = list(map(int,input().split()))
f = Counter(y)
list = []
for i in f.items():
  if(i[1] != 1):
    print(i[0],end = " ")
for j in f.items():
  list.append(j[1])
if(max(list) == 1):
  print("unique")
