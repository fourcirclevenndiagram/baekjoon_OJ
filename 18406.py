n = input()
middle = int(len(n) / 2)
a, b = sum(map(int, n[:middle])), sum(map(int, n[middle:]))
if(a == b):
    print("LUCKY")
else:
    print("READY")