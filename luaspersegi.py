# Fungsi mencari luas persegi panjang

def luaspersegipanjang (panjang, lebar):
    return panjang*lebar

# Fungsi mencari keliling persegi panjang
def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)
p= int(input("masukan nilai panjang: "))
l= int(input("masukan nilai lebar: "))

#panjang=(int(input("masukan nilai panjang: ")))
#lebar=(int(input("masukan nilai lebar: ")))

# Nilai luas panjang= 10, dan lebar= 5
hasil_luas = luaspersegipanjang(p,l)
hasil_keliling = kelilingpersegipanjang (p,l)
print("luasnya adalah ", hasil_luas)
print("kelilingnya adalah ", hasil_keliling)
