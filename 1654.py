k, n = map(int, input().split())
l_c = []
for i in range(k):
    l_c.append(int(input()))
start, end = 1, max(l_c)

while(start <= end):
    mid = (start+end) // 2
    l = 0
    for i in l_c:
        l += i // mid    
    if(l >= n):
        start = mid+1
    else:
        end = mid-1

print(end)