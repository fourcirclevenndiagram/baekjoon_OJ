'''
import sys
n, m = map(int, input().split())
drawer = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    tot = 0
    for j in range(a-1, b):
        tot += drawer[j]
    print(tot)
'''
import sys
n, m = map(int, sys.stdin.readline().split())

drawer = list(map(int, sys.stdin.readline().split()))
new_drawer = [0]
tot = 0  

for i in drawer:
    tot += i
    new_drawer.append(tot)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(new_drawer[b] - new_drawer[a-1])
