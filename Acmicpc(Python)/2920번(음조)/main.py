recoding = list(map(int, input().split()))
is_asc = bool()
is_des = bool()

for i in range(len(recoding)-1):
    if recoding[i] + 1 == recoding[i+1]:
        is_asc = True
    else:
        is_asc = False
        break

for i in range(len(recoding) - 1):
    if recoding[i] - 1 == recoding[i+1]:
        is_des = True
    else:
        is_des = False
        break

if is_asc:
    print("ascending")
elif is_des:
    print("descending")
else:
    print("mixed")