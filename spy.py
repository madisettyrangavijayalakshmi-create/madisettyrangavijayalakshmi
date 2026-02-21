n = int(input())
sum_d = 0
prod_d = 1
while n > 0:
    d = n % 10
    sum_d += d
    prod_d  *= d
    n //=  10
if sum_d == prod_d:
    print("Spy number")
else:
    print("not a spy number")
