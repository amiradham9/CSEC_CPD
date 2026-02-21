n=int(input())
wire=list(map(int,input().split()))
m =int(input())
for i in range(m):
    x,y=list(map(int,input().split()))
    if x !=1:
        wire[x-2] +=( y-1)
    if x!= n:
        wire[x] += (wire[x-1]-y)
    wire[x-1]=0
for i in range(n):
    print(wire[i])
