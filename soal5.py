def print_pattern(n):  #membuat fungsi print_pattern dengan parameter n
    for i in range(1, n+1):  #membuat loop for
        print(f"{i} " * i)  #f-string menghasilkan string berisi nilai i

n = int(input("Masukkan nilai n: "))  #menginput nilai dan mengubah menjadi integer dan disimpan dalam variabel n
print_pattern(n)  #memanggil fungsi print_pattern dengan n sebagai argumen