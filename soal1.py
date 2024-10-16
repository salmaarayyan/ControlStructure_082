def evaluate_performance(percentage):  #membuat fungsi evaluate_performance dengan parameter percentage
    if percentage >= 90:  #membuat kondisi dengan if
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else: #jika semua kondisi diatas tidak terpenuhi
        return "Below average performance"

percentage = float(input("Masukkan persentase nilai siswa: "))  #pengguna memasukkan angka dan akan disimpan dalam variabel percentage
result = evaluate_performance(percentage)  #memanggil fungsi evaluate_performance dengan percentage dan menyimpan hasil di variabel result
print(result)  #mencetak nilai result