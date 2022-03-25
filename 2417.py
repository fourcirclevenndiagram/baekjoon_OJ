import math
n = int(input())
ans = int(math.sqrt(n))
if(ans**2 == n):
    print(ans)
else:
    print(ans+1)