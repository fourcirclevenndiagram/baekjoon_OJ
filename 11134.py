t = int(input())
for i in range(0, t):
    a, b = input().split()
    a, b = int(a), int(b)
    ans = a // b
    if(a%b != 0):
        ans += 1
    print(ans)
    