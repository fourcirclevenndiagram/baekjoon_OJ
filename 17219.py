n, m = map(int, input().split())
drawer_dic = {}
for i in range(0, n):
    url, pw = input().split()
    drawer_dic[url] = pw
    
for i in range(0, m):
    temp = input()
    print(drawer_dic[temp])