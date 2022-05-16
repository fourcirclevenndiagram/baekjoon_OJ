n, w, h, l = map(int, input().split())
ans = (w//l) * (h//l)
if(ans > n):
    print(n)
else:
    print(ans)