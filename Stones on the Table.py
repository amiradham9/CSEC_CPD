n=int(input())
colors=list(input())
renove=0
for i in range(n-1):
    if colors[i] == colors[i+1]:
        renove += 1
print(renove)
