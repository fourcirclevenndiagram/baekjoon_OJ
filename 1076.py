fac1 = 10
fac2 = 1
fac3 = 1
lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

p1 = input()
p2 = input()
p3 = input()

for i in range(10):
    if(p1 == lst[i]):
        fac1 *= i
    if(p2 == lst[i]):
        fac2 *= i
    if(p3 == lst[i]):
        fac3 *= (10**i)
print((fac1+fac2) * fac3)