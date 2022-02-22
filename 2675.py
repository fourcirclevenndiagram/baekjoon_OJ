n = int(input())

for i in range(0, n):
    r, s = input().split()
    r = int(r)
    for j in range(0, len(s)):
        for k in range(0, r):
            print(s[j], end='')
    print()