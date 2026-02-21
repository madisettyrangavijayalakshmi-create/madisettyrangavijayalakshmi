n = int(input())
temp = n
digits = len(str(n))
sum_val = 0
while temp > 0:
    d = temp % 10
    sum_val += d ** digits
    temp //=  10
if sum_val == n:
    print("armstrong number")
else:
    print("not a armstrong number")
