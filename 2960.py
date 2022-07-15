n, k = map(int, input().split())
cnt = 0
my_num = ["T"] * (n+1)

for i in range(2, len(my_num) + 1):
    for j in range(i, n+1, i):
        if my_num[j] == "T":
            my_num[j] = "F"
            cnt += 1
            if cnt == k:
                print(j)
                break