n = int(input())
words = []                # 입력받은 문자열을 담을 리스트
scan_length = 0           # 문자열 길이가 작은 순서대로 정렬할 때 쓰는 리스트
sorted_words = []         # 정렬된 문자열을 담을 리스트
scan_idx = 0              # 두 문자열 비교할 때, n번째 문자를 비교할 때 쓰는 인덱스번호
level = 1                 # 문자열 길이가 같은 문자열끼리 비교하기 위해서 마련한 변수
for i in range(0, n):     # n개의 단어를 엔터로 구분하여 입력받음
    words.append(input())

words = list(set(words))
words.sort()

while(1):  
    scan_length += 1
    for i in range(0, len(words)):
        if(len(words[i]) == scan_length):
            temp = words[i]
            sorted_words.append(temp)
    if(len(words) == len(sorted_words)):
        break

for i in range(0, len(sorted_words)):
    print(sorted_words[i])
