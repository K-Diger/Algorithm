arr = [1,2,3,4]

def solution(arr):
    answer = int(0)
    for i in range(len(arr)):
        answer += int(arr[i])
    return float(answer/len(arr))

    # return sum(arr)/len(arr)

print(solution(arr))