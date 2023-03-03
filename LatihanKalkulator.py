angka1 = float(input("masukkan angka 1 : "))
angka2 = float(input("masukkan angka 2 : "))
operator = input("operator : ")

if operator == "+" :
    hasil = angka1 + angka2
    print(angka1, "+" , angka2, "=", hasil )

elif operator == "-" :
    hasil = angka1 - angka2
    print(angka1, "=", angka2, "=", hasil)

elif operator == "*" :
    hasil = angka1 * angka2
    print(angka1, "*", angka2, "=", hasil)
    
elif operator == "/" :
    hasil = angka1 / angka2
    print(angka1, "/", angka2, "=", hasil)

else : 
    print("Input salah")

print("See you!")