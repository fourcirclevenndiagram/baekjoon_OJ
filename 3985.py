l = int(input())
n = int(input())
order_list = []
expected = []
roll_cake = [1]*(l+1)
take_cake = [0]*(n+1)
for i in range(n):
    start, end = list(map(int, input().split()))
    order_list.append([start,end])
    expected.append(end-start)
    
for i in range(n):
    start = order_list[i][0]
    end = order_list[i][1]
    for j in range(start, end+1):
        if(roll_cake[j] != 0):
            roll_cake[j] = 0
            take_cake[i+1] += 1
expected_max = expected.index(max(expected))+1
real_max = take_cake.index(max(take_cake))
print(expected_max)
print(real_max)