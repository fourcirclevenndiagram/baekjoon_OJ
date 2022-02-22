a = input()
a = list(a)
half = len(a)//2
a.insert(half, ' ')
print(''.map(join(str, a)))
