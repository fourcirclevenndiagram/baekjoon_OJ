a, b = 0, 0
while(not ((0 < a and a < 10) and (0 < b and b < 10))):
    a, b = input().split()
    a, b = int(a), int(b)
print(a/b)