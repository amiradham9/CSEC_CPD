word=list(input())
count=0
for i in range(len(word)):
    if i==0:
        c_w=ord(word[0])-ord("a")
    else:
        c_w=abs(ord(word[i])-ord(word[i-1]))
    cc_w=26-c_w
    count +=min(c_w,cc_w)
print(count)
