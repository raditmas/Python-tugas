def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print("Deret Fibonacci sampai 20 bilangan pertama:")
for i in range(1,7 ):
    print(f"Fibo({i}) = {fibo(i)}")