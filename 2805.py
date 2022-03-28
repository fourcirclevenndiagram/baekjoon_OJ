n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = max(trees)
axe = start
flag = 0
while(1):
    gain_tree = 0
    for i in trees:
        if(i > axe):
            gain_tree += (i - axe)
    if(gain_tree > m):
        flag = 1
        break
    axe -= 1
print(axe)