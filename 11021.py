t = input()
t = int(t)
case = []
for i in range(0, t):
    a, b = input().split()
    a, b = int(a), int(b)
    case.append(a+b)
for j in range(0, t):
    print("Case #%d: %d"%(j+1, case[j]))
