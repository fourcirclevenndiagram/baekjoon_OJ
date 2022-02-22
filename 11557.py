# print("테스트 케이스 수를 입력하세요")
t = input()
t = int(t)
winner = []
for i in range(0, t):
    # print("%d번째 케이스입니다"%(i+1))
    # print("학교 수를 입력하세요")
    n = input()
    n = int(n)
    best = {'school':'', 'alcohol':0}
    for_comp = []
    j = 0
    while(j < n):
        same = 0
        # print("%d 번째 학교 이름과 주량을 입력하세요"%(j+1))
        school, alcohol = input().split()
        alcohol = int(alcohol)
        for_comp.append(alcohol)
        if(j > 0):
            for comp in range(0, j):
                if(for_comp[comp] == alcohol):
                    same += 1
                    break
        j += 1
        if(same > 0):
            # print("같은 주량의 학교가 있습니다! 재입력해주세요")
            j -= 1            

        if(same == 0 and alcohol > best['alcohol']):
            best['school'] = school
            best['alcohol'] = alcohol
        
    winner.append(best['school'])
for i in range(0, t):
    print(winner[i])

# Clear
# 안내 멘트를 print 하는 코드를 넣으면 '출력 초과'로 실패