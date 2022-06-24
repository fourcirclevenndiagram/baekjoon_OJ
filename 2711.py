t = int(input())
for i in range(t):
    a, b = input().split()
    idx = int(a) - 1
    sentence = list(b)
    sentence.pop(idx)
    sentence = ''.join(map(str, sentence))
    print(sentence)