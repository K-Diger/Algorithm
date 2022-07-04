def solution(numbers, hand):
    answer = ''

    left_hand_area = [1, 4, 7]
    right_hand_area = [3, 6, 9]
    middle_hand_area = [2, 5, 8, 0]

    current_left_hand = int(10)
    current_right_hand = int(11)

    for number in numbers:

        if number == 0:
            number = 11

        if number in left_hand_area:
            answer += 'L'
            current_left_hand = number

        elif number in right_hand_area:
            answer += 'R'
            current_right_hand = number

        elif number in middle_hand_area:
            if abs(current_left_hand - number) > abs(current_right_hand - number):
                answer += 'R'
                current_right_hand = number

            elif abs(current_left_hand - number) < abs(current_right_hand - number):
                answer += 'L'
                current_left_hand = number

            # 왼손/오른손 잡이 검증
            else:
                if hand == "right":
                    answer += 'R'
                    current_right_hand = number
                else:
                    answer += 'L'
                    current_left_hand = number
    print(answer)

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

solution(numbers, hand)
