# input nilai variable
a=input ("masukan nilai a:")
b=input ("masukan nilai b:")

# cetak nilai variable
print("variable a=",a)
print("variable b=",b)

#cetak hasil operasi kedua variable dengan string format
print("hasil penggabung {}&{}=%o". format (a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan {}+{}=%d". format (a,b) %(a+b))
print("hasil pembagian {}/{}=%d". format (a,b) %(a/b))

