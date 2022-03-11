'''
import sys
a, b, c = map(int, sys.stdin.readline().split())
i = 0
fail = 0
if(b > c):
    fail += 1
cost = a
profit = 0
flag = 0
while(b < c and cost >= profit):    
    i += 1
    # if(a+(b*i) < c*i):
    #     break
    cost += b
    profit += c
if(fail):
    print(-1)
else:
    print(i)

# 시간초과
'''
import sys
a, b, c = map(int, sys.stdin.readline().split())
if(b >= c):
    print(-1)
else:
    print(int(a/(c-b)+1))