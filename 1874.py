n = int(input())
my_stack = []
action = []
level = 1
flag = 0
for i in range(n):
    n = int(input())
    while(1):
        if(level > n):
            break
        my_stack.append(level)
        level += 1
        action.append('+')
    if(my_stack[len(my_stack)-1] == n):
        my_stack.pop()
    else:
        flag = 1
        break
if(flag):
    print("NO")
else:
    for i in range(0, len(action)):
        print(action[i])