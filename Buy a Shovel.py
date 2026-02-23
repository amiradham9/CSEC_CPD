k,r=list(map(int,input().split()))
count=1
m=k
while True:
    if (m-r) %10==0 or m % 10==0:
        break
    count += 1
    m =k* count
print(count)
