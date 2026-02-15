n=int(input())
count=0
m=0
for _ in range(n):
    k=int(input())
    if (k != m):
        m = k
        count += 1
print(count)
