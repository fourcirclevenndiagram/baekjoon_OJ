t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    ans = 0
    
    for j in range(n):
        px, py, r = map(int, input().split())
        a = (((x1-px) ** 2) + ((y1-py) ** 2)) ** 0.5
        b = (((px-x2) ** 2) + ((py-y2) ** 2)) ** 0.5
        
        if a < r:
            ans += 1
        elif b < r:
            ans += 1

    print(ans)