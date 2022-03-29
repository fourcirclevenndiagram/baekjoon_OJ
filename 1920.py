import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

def bin_search(start, end, unit, the_list):
    if start > end:
        return 0
    mid = int((start+end)/2)
    if(the_list[mid] == unit):
        return 1
    elif(the_list[mid] > unit):
        return bin_search(start, mid-1, unit, the_list)
    else:
        return bin_search(mid+1, end, unit, the_list)

for i in b:
    start = 0
    end = len(a)-1
    ans = bin_search(start, end, i, a)
    print(ans)