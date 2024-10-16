def print_odd_numbers(n):  #membuat fungsi print_odd_numbers dengan parameter n
    for i in range(1, n+1):  #memulai loop for yang akan berjalan dari 1 hingga n dan menghasilkan bilangan dari 1 hingga n
        if i % 2 != 0:  #memeriksa apakah i adalah bilangan ganjil
            print(i, end=" ")  #jika i bilangan ganjil, maka cetak nilai i

n = int(input("Masukkan batas bilangan ganjil: "))  #memasukkan nilainya dan nilai input menjadi integer dan disimpan dalam variabel n
print_odd_numbers(n)  #memanggil fungsi print_odd_numbers dengan n sebagai argumen untuk mencetak bilangan ganjil