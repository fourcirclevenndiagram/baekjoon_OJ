original = input()
bomb = input()

drawer = []

for c in original:
    drawer.append(c)
    if(c == bomb[-1] and ''.join(drawer[-(len(bomb)):]) == bomb):
        del drawer[-(len(bomb)):]

ans = ''.join(drawer)

if(ans == ''):
    print("FRULA")
else:
    print(ans)
