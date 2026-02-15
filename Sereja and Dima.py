n=int(input())
card_numbers=list(map(int,input().split()))
serehja_p=0
Dima_p=0
for i in range(n):
    if card_numbers[0]>card_numbers[-1]:
        maximum=card_numbers[0]
        card_numbers.pop(0)
    elif card_numbers[0]< card_numbers[-1]:
        maximum=card_numbers[-1]
        card_numbers.pop(-1)
    else:
        maximum=card_numbers[-1]
        card_numbers.pop(-1)

    if i%2==0:
        serehja_p += maximum
    else:
        Dima_p += maximum
print(serehja_p,Dima_p)   
