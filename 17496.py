a, b, c, d = map(int, input().split())
fruits = 0
for i in range(1, a+1, b):
    fruits += 1
print((fruits-1) * c * d)