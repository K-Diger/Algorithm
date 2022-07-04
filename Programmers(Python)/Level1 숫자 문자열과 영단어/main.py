import re

def solution(s):
    string_number_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                     "eight": 8, "nine": 9}

    for key in string_number_dict:
        s = re.sub(f"{key}", f"{string_number_dict[key]}", s)


    return int(s)


s = "one4seveneight"


solution(s)