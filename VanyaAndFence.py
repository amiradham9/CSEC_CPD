n,l=list(map(int,input().split()))
hight=list(map(int,input().split()))
width=n
for i in range(n):
    if hight[i]>l:
        width += 1
print(width)
