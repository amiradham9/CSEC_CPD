n=int(input())
winner=list(input())
countA=0
countB=0
for i in range(n):
    if winner[i]=="A":
        countA += 1
    else:
        countB += 1
if countA > countB :
    print("Anton")
elif countA < countB :
    print("Danik")
else:
    print("Friendship")
