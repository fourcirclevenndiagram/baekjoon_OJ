c = int(input())
for i in range(c):
    temp = list(map(int, input().split()))
    scores = temp[1:]
    average = sum(scores) / len(scores)
    print("%d%%"%(round(average, 3)))