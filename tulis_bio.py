# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input(" Alamat: ")
# format teks
teks ="Nama : {}\nUmur: {}\nAlamatn: {}\n".format(nama, umur, alamat)
# buka file untuk ditulis
file_bio = open("biodata.txt", "a")
# tulis teks file
file_bio.write(teks)
# tutup file
file_bio.close()