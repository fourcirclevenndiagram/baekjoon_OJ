n = int(input())
def f(num):
    ans = 1
    if(not num):
        return 1
    else:
        for i in range(1, num+1):
            ans *= i
        return ans
print(f(n))