a, b = map(int, input().split())
i = 1
while(a*i % b != 0):
    i += 1
print(a*i)
if(b > a):
    a, b = b, a
while(a % b != 0):
    a, b = b, a-b
print(b)