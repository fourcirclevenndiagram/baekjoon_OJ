data = input()
finding = input()
len_f = len(finding)
start = 0
cnt = 0

while(start <= len(data) - len_f):
    if(data[start:start+len_f] == finding):
        cnt += 1
        start += len_f
    else:
        start += 1

print(cnt)