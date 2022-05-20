n = int(input())
ans = 0
for i in range(n):
    word = input()
    show_again = False
    for j in range(len(word)-1):
        if(word[j] != word[j+1]):
            tmp = word[(j+1):]
            if(word[j] in tmp):
                show_again = True
    if(show_again == False):
        ans += 1
print(ans)