print("테스트 케이스 수를 입력하세요")
t = input()
t = int(t)
winner = []
for i in range(0, t):
    print("학교 수를 입력하세요")
    n = input()
    n = int(n)
    best = {'school':'', 'alcohol':0}
    for_comp = []
    for j in range(0, n):
        same = 0
        print("%d 번째 학교 이름과 주량을 입력하세요"%(j+1))
        school, alcohol = input().split()
        alcohol = int(alcohol)
        for_comp.append(alcohol)
        if(j > 0):
            for comp in range(0, j):
                if(for_comp[comp] == alcohol):
                    same += 1
                    break
        if(same > 0):
            j -= 1
            continue

        if(alcohol > best['alcohol']):
            best['school'] = school
            best['alcohol'] = alcohol
    winner.append(best['school'])
for i in range(0, t):
    print(winner[i])
    