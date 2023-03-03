#memasukkan data tanpa casting maka tipe data otomatis string
data = input("masukkan data = ")
print("data =", data, type(data))

#melakukan casting tipe data yang di input
data = str(input("masukkan angka = "))
print("data = ", data, type(data))

#melakukan casting tipe data string ke float
nilai = float(input("masukkan nilai ="))
print("nilai =", nilai,type(nilai))

#melakukan casting tipe data string ke int
skor = int(input("masukkan skor ="))
print("skor =", skor,type(skor))

#melakukan casting pada boolean maka harus dicasting ke int terlebih dahulu
biner = bool(int(input("masukkan nilai boolean :")))
print("data=", biner,"type", type(biner))