odds = []
the_sum = 0
for i in range(7):
    a = int(input())
    if(a%2 == 1):
        odds.append(a)
        the_sum += a
print(the_sum)
print(min(odds))