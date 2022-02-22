sentence = input()
flag = 0
words = 0
for i in range(0, len(sentence)):
    if(flag == 0 and sentence[i] != ' '):
        words += 1
        flag = 1
    elif(sentence[i] == ' '):
        flag = 0
print(words)