def find_largest(a, b, c):  #membuat fungsi find_largest dengan parameter a,b,c
    if a >= b and a >= c:  #membuat kondisi if
        return a
    elif b >= a and b >= c:  #jika kondisi diatas tidak terpenuhi
        return b
    else:  #jika kedua kondisi diatas tidak terpenuhi
        return c

a = float(input("Masukkan angka pertama: "))  #pengguna memasukkan angka dan disimpan dalam variabel a
b = float(input("Masukkan angka kedua: "))  #pengguna memasukkan angka dan disimpan dalam variabel b
c = float(input("Masukkan angka ketiga: "))  #pengguna memasukkan angka dan disimpan dalam variabel c

largest = find_largest(a, b, c)  #memanggil fungsi find_largest dengan a,b,c sebagai argumen dan disimpan di variabel largest
print(f"Bilangan terbesar adalah: {largest}")  #mencetak hasil dengan f-string, guna f untuk bisa memasukkan float ke string