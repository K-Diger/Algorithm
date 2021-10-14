#이항계수 공식
# n! // k!(n-k)!

n, k = map(int, input().split())

temp = int(1) # n!
temp_ = int(1) # k!
temp__ = int(1) # (n-k)!
res = int()

for x in range(1, n+1): #n!
    temp *= x

for y in range(1, k+1): #k!
    temp_ *= y

for z in range(1, (n-k)+1):
    temp__ *= z


print(temp//(temp_*temp__))