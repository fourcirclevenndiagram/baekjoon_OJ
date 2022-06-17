n = int(input())
cars = list(map(int, input().split()))
cnt = 0

for i in range(len(cars)) :
  if(cars[i] == n):
    cnt += 1

print(cnt)