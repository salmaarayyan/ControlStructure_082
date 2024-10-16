def fibonacci(n):  #membuat fungsi fibonacci dengan parameter n
    fib = [0, 1]  #inisialisasi fib dengan 2 angka pertama deret fibonacci, yaitu 0 dan 1
    while len(fib) < n:  #membuat loop while dan akan berjalan selama fib < n
        fib.append(fib[-1] + fib[-2])  #append itu metode menambah data tanpa merubah data sebelumnya. fib[-1] adalah emen terakhir dari list dan fib[-2] adalah elemen kedua dari terakhir
    return fib[:n]

n = int(input("Masukkan jumlah angka Fibonacci yang diinginkan: "))  #pengguna meginput angka fibonacci dan mengubah input menjadi integer dan disimpan dalam variabel n
result = fibonacci(n)  #memanggil fungsi fibonacci dengan n sebagai argumen dan menyimpan hasil dalam variabel result
print(f"Deret Fibonacci hingga {n} angka: {result}")  #mencetak hasil