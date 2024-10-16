def print_pattern(n):
    for i in range(1, n+1):
        print(f"{i} " * i)

n = int(input("Masukkan nilai n: "))
print_pattern(n)