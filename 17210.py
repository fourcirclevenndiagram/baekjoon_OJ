n = input()
n = int(n)
op = input()
fail = 0
history = []
if(op == '0'):
    key2, key3 = '1', '0'
else:
    key2, key3 = '0', '1'

for i in range(1, n+1):
    history.append(op)
    if(i%2 == 0 and op != key2):
        fail += 1
        break
    if(i%3 == 0 and op != key3):
        fail += 1
        break
    if(op == '0'):
        op = '1'
    else:
        op = '0'

if(fail):
    print("Love is open door")
else:
    for i in range(0, n):
        print(history[i])

