k, n = map(int, input().split())

lan_cable = [int(input()) for i in range(k)]
min_cable = min(lan_cable)

res = sum(lan_cable) // int(n)

res_ = min_cable * n

print(res)
print(res_)