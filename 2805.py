import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = max(trees), 0
# while(1):
#     gain_tree = 0
#     for i in trees:
#         if(i > axe):
#             gain_tree += (i - axe)
#     if(gain_tree > m):
#         flag = 1
#         break
#     axe -= 1
while(start >= end):
    mid = (start+end) // 2
    cut_tree = 0
    for i in trees:
        if(i > mid):
            cut_tree += (i - mid)
    if(cut_tree >= m):
        end = mid+1
    else:
        start = mid-1
print(start)