A, a, B, b, P = input().split()
A, a, B, b, P = int(A), int(a), int(B), int(b), int(P)

flag = 0

if(P > B and B > b and b > A and A > a and a > 0 and A > 0 and b > 0 and B > 0 and P > 0 and a <= 1000000 and A <= 1000000 and b <= 1000000 and B <= 1000000 and P <= 1000000):
    flag += 1
if(flag > 0):
    print("Yes")
elif(flag == 0):
    print("No")