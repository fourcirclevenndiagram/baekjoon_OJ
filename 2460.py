_on = 0
tmp = 0

for i in range(10):
    n, m = map(int, input().split())
    _on += m - n
    tmp = max(tmp, _on)
print(tmp)