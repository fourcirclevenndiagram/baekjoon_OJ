n, k = input().split()
n, k = int(n), int(k)
theMap = []
newMap = []
drawer = []

for i in range(0, n):
    inp = input().split()
    theMap.append(inp)
for i in range(0, n):          # n의 길이 수 만큼 반복
    for j in range(0, k):      # k배만큼 세로 길이를 늘림
        for l in range(0, k):  # theMap의 i번째 행을 훑으며 k배만큼 가로 길이를 늘림
            drawer.append(theMap[i][n])