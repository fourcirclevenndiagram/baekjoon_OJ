import sys

n, k = map(int, sys.stdin.readline().split())
my_coin = []
pay = 0
for i in range(0, n):
    temp = int(sys.stdin.readline())
    my_coin.append(temp)
i = 0
while(k > 0):
    if(k >= my_coin[len(my_coin)-i-1]):        
        pay += k // my_coin[len(my_coin)-i-1]
        k %= my_coin[len(my_coin)-i-1]
    else:
        i += 1
print(pay)