n = input()
n = int(n)
pieces = 1
for i in range(0, n):
    pieces += (i+1)//2+1
print(pieces)