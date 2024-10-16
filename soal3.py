def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Masukkan jumlah angka Fibonacci yang diinginkan: "))
result = fibonacci(n)
print(f"Deret Fibonacci hingga {n} angka: {result}")