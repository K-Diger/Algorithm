'''


일단 report의 value 값을 다 비교할거임 같은게 있으면

추가 딕셔너리 value ++

그렇게 한 후 딕셔너리 value 가 k 이상인게 있으면

그 value 를 value로 가진 report 딕셔너리의 key를 불러오고

그 key 의 값을 +1

'''

def solution(id_list, report, k):

    id_dict = {item: 0 for item in id_list}
    reported_dict = {item: 0 for item in id_list}
    report = set(report)

    # report_item 에는, "muzi frodo", "apeach frodo" ... 등 중복이 제거된, 공백으로 구분된 신고 정보가 담겨있음
    for report_item in report:
        # reported_dict 에 신고된 아이디를 Key 로 잡고, 그 Value 또한 1씩 증가시킴
        reported_dict[report_item.split()[1]] += 1

    for report_item in report:
        # 위 반복문에서 셋팅한 딕셔너리에
        # reported_dict[report_item.split()[1] 에는 신고당한 유저들 아이디가 있다.
        # 그래서, reported_dict 에서 신고당한 아이디를 Key 가지는 Value 를 뽑았을 때 그게 K보다 크면
        if reported_dict[report_item.split()[1]] >= k:
            # id_dict 에서 Key 에 해당하는 Value 를 1 증가시킨다.
            id_dict[report_item.split()[0]] += 1

    return list(id_dict.values())






id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = int(2)

print(solution(id_list, report, k))