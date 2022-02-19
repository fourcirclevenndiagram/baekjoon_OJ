a, b = input().split()
a, b = int(a), int(b)
m = (b-a)/400
winning_rate = 1/(1+10**m)
print(winning_rate)