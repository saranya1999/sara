def portot(n1,array):
    for  x in range(0,n1-2):
        for y in range(x+1,n1-1):
            for z in range(y+1,n1):
                if array[x]+array[y] == array[z]:
                    print(array[x], array[y], array[z])
n1=int(input())
array=list(map(int,input().split()))
portot(n1,array)
