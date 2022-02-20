on = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
ans = []
while(1):
    obj = input().split()
    if(obj[0] == "***"):
        break
    n = input()
    n = int(n)
    for i in range(0, len(obj)):
        j = (i+n)%12
        ans.append(obj[j])
    print(ans)