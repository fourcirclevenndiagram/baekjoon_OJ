a, b = input().split()
ans = bin(int(a, 2) + (int(b, 2)))
for i in range(2, len(ans)):
    print(ans[i], end='')