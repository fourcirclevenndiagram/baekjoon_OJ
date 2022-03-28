n = int(input())
m = int(input())
com_list = []
for i in range(n):
    com_list.append([])

for i in range(m):
    com1, com2 = map(int, input().split())
    com_list[com1-1].append(com2-1)
    com_list[com2-1].append(com1-1)

ding_dong = 0
visited_list = [0] * n

def dfs(start_node):
    global ding_dong
    visited_list[start_node] = 1
    for i in com_list[start_node]:
        if(not visited_list[i]):
            dfs(i)
            ding_dong += 1
dfs(0)
print(ding_dong)
