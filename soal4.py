def print_odd_numbers(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")

n = int(input("Masukkan batas bilangan ganjil: "))
print_odd_numbers(n)