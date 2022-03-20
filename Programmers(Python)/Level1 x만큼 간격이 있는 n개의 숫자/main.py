def solution(x, n):
    answer = [x]
    for i in range(n):
        answer.append(answer[i] + x)

    return answer[0:n]