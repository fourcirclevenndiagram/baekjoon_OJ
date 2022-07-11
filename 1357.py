x, y = input().split()

def sol(n):
    n = int(n[::-1])
    return n

ans = sol(str(sol(x)+sol(y)))
print(ans)