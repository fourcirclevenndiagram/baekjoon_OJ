t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    jungyo = list(map(int, input().split()))
    idx = list(range(len(jungyo)))
    idx[m] = 'target'

    order = 0
    
    while(1):
        if(imp[0] == max(imp)):
            order += 1

            if(idx[0]=='target'):
                print(order)
                break
            else:
                jungyo.pop(0)
                idx.pop(0)

        else:
            jungyo.append(jungyo.pop(0))
            idx.append(idx.pop(0))    