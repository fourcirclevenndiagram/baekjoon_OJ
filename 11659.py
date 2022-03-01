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
n, m = map(int, input().split())

drawer = list(map(int, input().split()))
new_drawer = [0]
tot = 0  

for i in range(0, n):
    tot += drawer[i]
    new_drawer.append(tot)
for i in range(0, m):
    a, b = map(int, input().split())
    print(new_drawer[b] - new_drawer[a-1])
