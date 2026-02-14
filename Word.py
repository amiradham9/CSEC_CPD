text=input()
count = sum(1 for char in text if char.isupper())
print(count)
if count > len(text)/2:
    print(text.upper())
else:
    print(text.lower())
