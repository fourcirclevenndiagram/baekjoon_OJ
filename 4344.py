c = int(input())
for i in range(c):
    temp = list(map(int, input().split()))
    scores = temp[1:]
    average = sum(scores) / len(scores)
    winner = 0
    for j in scores:
        if(j > average):
            winner += 1
    ans = winner / len(scores) * 100
    # print("%d%%"%(round(ans, 3)))
    print(f'{ans:.3f}%')