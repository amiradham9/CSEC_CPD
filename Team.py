n=int(input())
counter=0
for _ in range(n):
    num=list(map(int,input().split()))
    if (num.count(1) >= 2):
        counter += 1
print(counter)
