a = []
i = 0
tot = 0
while(i < 5):
    #print("%d번째 학생의 점수 (5의 배수)를 입력하세요"%(i+1))
    score = int(input())
    if(score < 40):
        score = 40
    a.append(score)
    
    i += 1
for i in range(0, 5):
    tot += a[i]
avr = int(tot/5)
print(avr)