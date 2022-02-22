e, em, m, mh, h = input().split()
e, em, m, mh, h = int(e), int(em), int(m), int(mh), int(h)


E, M, H = 0, 0, 0  # 대회에 출제할 난이도별 문제 수
proper_num = (e + em + m + mh + h) / 3 # 개최를 최대한 많이 할 수 있도록 하기 위한 적정 난이도별 문제수
contest = 0        # 개최 가능한 대회 수

# 확정 난이도 문제부터 분배
for i in range(0, e):
    e -= 1
    E += 1
for i in range(0, m):
    m -= 1
    M += 1
for i in range(0, h):
    h -= 1
    H += 1
# 확정 난이도 분배 확인
## print(E, M, H)

# 애매 난이도 문제 분배
for i in range(0, em):
    if(E > M):
        em -= 1
        M += 1
    elif(E < M):
        em -= 1
        E += 1
    else:
        break

for i in range(0, mh):
    if(M > H):
        mh -= 1
        H += 1
    elif(M < H):
        mh -= 1
        M += 1
    else:
        break
 
print(E, em, M, mh, H, proper_num)
# 대회에 사용할 문제를 배분
while(E > 0 and M > 0 and H > 0):
    E -= 1
    M -= 1
    H -= 1
    contest += 1

print(contest)