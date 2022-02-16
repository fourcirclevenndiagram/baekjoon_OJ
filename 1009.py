t = 0
a, b = 0, 0
while(t <= 0):
    t = input()
    t = int(t)

while(not ((1 <= a and a <= 100) and (1<= b and b <= 1000000))):
    a, b = input().split()
    a, b = int(a), int(b)

print((a**b)//10)