t = input()
t = int(t)
i = 0
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
while(i < t):
    a, b = input().split()
    a, b = int(a), int(b)
    if(a == 0 or b == 0):
        axis += 1
    elif(a > 0 and b > 0):
        q1 += 1
    elif(a < 0 and b > 0):
        q2 += 1
    elif(a < 0 and b < 0):
        q3 += 1
    elif(a > 0 and b < 0):
        q4 += 1
    i += 1
print("Q1: %d"%q1)
print("Q2: %d"%q2)
print("Q3: %d"%q3)
print("Q4: %d"%q4)
print("AXIS: %d"%axis)