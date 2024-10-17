# Input ekspresi matematika
ekspresi = input("Masukkan operasi (misalnya 5 + 2, 4 * 3): ")

    # Menggunakan eval untuk evaluasi ekspresi matematika
try:
    hasil = eval(ekspresi) 
    print("Hasil: " , hasil)
except ZeroDivisionError :
    print("Tidak bisa membagi dengan nol")
except Exception :
    print("Ekspresi tidak valid")
