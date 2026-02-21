s = "hello"
vowels = "aeiouAEIOU"
s = list(s)
left = 0
right = len(s)-1
while left < right:
    if s[left] not in vowels:
        left += 1
    elif s[right] not in vowels:
        right -= 1
    else:
        temp = s[right]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
        result =" "
for ch in s:
    result += ch
print("reverse vowels result:",result)
    
