n=int(input())
event=list(map(int,input().split()))
crime=0
hired=0
for i in range(n):
    if event[i] ==-1:
        if hired == 0:
            crime +=1
        else:
            hired -= 1
    else:
        hired += event[i]
print(crime)
