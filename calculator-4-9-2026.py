p = True
while p == True:
    print("Ketik 'a' untuk tambah, 'b' untuk kurang, 'c' untuk kali dan 'd' untuk bagi.")
    operasi = input("mau operasi apa?").lower()
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    if operasi == 'a':
        hasil = num1+num2
        print("Hasil:", hasil)
    elif operasi =='b':
        hasil = num1-num2
        print("Hasil:", hasil)
    elif operasi =='c':
        hasil = num1*num2
        print("Hasil:", hasil)
    elif operasi =='d':
        hasil = num1/num2
        print("Hasil:", hasil)
    if hasil%2 ==0:
        print("angka genap")
    elif hasil%2 ==1:
        print("angka ganjil")
    else:
        print("Angka desimal")
    con = input("Would you like to try again?(yes/no)").lower()
    if con == 'no':
        p = False
    else:
        p = True
