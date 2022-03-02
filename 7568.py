n = int(input())
people = []
for i in range(n):
    temp = []
    temp.append(1)
    wei, hei = map(int, input().split())
    temp.append(wei)
    temp.append(hei)
    people.append(temp)
for i in range(n):        # 나
    for j in range(n):    # 상대
        if(people[i][1] < people[j][1] and people[i][2] < people[j][2]): # 나와 상대의 키, 몸무게를 비교. 둘 다 상대가 우위인지 확인
            people[i][0] += 1
for i in range(n):
    print("%d"%people[i][0], end = ' ')
print()
    