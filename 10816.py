import sys
from collections import Counter
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
# for i in range(m):
#     print("%d"%(a.count(b[i])), end = ' ')

cnt = Counter(a)
print(' '.join(f'{cnt[x]}' if x in cnt else '0' for x in b))