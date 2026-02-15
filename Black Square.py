a1,a2,a3,a4=list (map(int,input().split()))
a=list(input())
calories=0
for i in range(len(a)):
    if a[i]=="1":
        calories += a1
    elif a[i]=="2":
        calories += a2
    elif a[i]=="3":
        calories += a3
    else:
        calories +=a4

print(calories)
