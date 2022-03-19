my_word = input().upper()
for_cnt_word = list(set(my_word))
for_cnt_cnt = []


for i in range(len(for_cnt_word)):
    for_cnt_cnt.append(my_word.count(for_cnt_word[i]))
    print(for_cnt_cnt)
if(for_cnt_cnt.count(max(for_cnt_cnt)) > 1):
    print('?')
else:
    print(for_cnt_word[for_cnt_cnt.index(max(for_cnt_cnt))])