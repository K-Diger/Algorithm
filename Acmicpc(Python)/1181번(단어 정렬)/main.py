import sys

n = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip('\n') for i in range(n)]
sorted_words = []

for i in range(n): #중복 값 제거
    if words[i] in sorted_words:
        pass
    else:
        sorted_words.append(words[i])

sorted_words.sort() #기본 정렬함수로 사전순으로 Sort
sorted_words.sort(key=lambda x: len(x)) # 사전순으로 정렬된 배열에 + 길이 순으로 Sort

for i in range(len(sorted_words)):
    print(sorted_words[i])