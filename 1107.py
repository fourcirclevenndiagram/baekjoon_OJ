n = int(input())
m = int(input())
if(m > 0):
    broken_button = set(map(int, input().split()))
else:
    broken_button = set()
min_push_button = (100 - n)
if(min_push_button < 0):
    min_push_button = -min_push_button

for i in range(0, 1000001):
    i = str(i)
    for j in range(len(i)):
        if(int(i[j]) in broken_button):
            break
        elif(j == len(i)-1):
            temp = int(i) - n
            if(temp < 0):
                temp = -temp
            min_push_button = min(min_push_button, temp + len(i))

print(min_push_button)