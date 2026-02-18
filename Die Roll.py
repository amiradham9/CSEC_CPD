y,m=list(map(int,input().split()))
if max(y,m)==1:
    print("1/1")
elif max(y,m)==2:
    print("5/6")
elif max(y,m)==3:
    print("2/3")
elif max(y,m)==4:
    print("1/2")
elif max(y,m)==5:
    print("1/3")
else:
    print("1/6")
