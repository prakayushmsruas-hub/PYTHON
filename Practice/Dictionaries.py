s=input("Enter a string:")
freq={}
for ch in s:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]+=1
print(f"Frequency of characters:{freq}")            
dup={}
unique={}
for ch in s:
    if freq[ch]>1:
        dup[ch]=freq[ch]
    else:
        unique[ch]=1
print(f"Duplicate Characters:{dup}")
print(f"Unique Characters:{unique}")               