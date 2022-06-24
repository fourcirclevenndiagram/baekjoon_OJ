t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))