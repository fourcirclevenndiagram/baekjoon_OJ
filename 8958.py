n = int(input())
for i in range(0, n):
    s = input()
    get_score = 1
    tot_score = 0
    flag = 0
    for j in range(0, len(s)):
        if(s[j] == 'O'):
            if(flag == 1):
                get_score += 1
            tot_score += get_score
            flag = 1        
        else:
            flag = 0
            get_score = 1
    print(tot_score)