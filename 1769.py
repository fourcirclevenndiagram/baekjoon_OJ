n = input()
cnt = 0

def sol(ob, cnt):
    if(len(ob) > 1):
        cnt += 1
        tmp = 0
        for i in ob:
            tmp += int(i)
        sol(str(tmp), cnt)
    else:
        if(int(ob)%3):
            print(cnt)
            print("NO")
        else:
            print(cnt)
            print("YES")

sol(n, cnt)