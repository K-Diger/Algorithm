t = int(input())

fibo_arr = [0]*100
fibo_arr[0], fibo_arr[1] = 1, 1

def dp_fibo(n):
    if fibo_arr[n] == 0:
        fibo_arr[n] = dp_fibo(n-1)+dp_fibo(n-2)

    return fibo_arr[n]

print(dp_fibo(t))