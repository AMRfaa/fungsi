# Fugnsi mencari nilai faktoril
def faktorial (n) :
    if n==0 or n==1 :
        return 1
    else :
        return n*(faktorial(n-1))

# Mencari nilai faktorial!
a = int(input("Masukan nilai yangg akan dicari: "))
cari_faktorial= faktorial(a)
print ("Nilai dari", a, "! adalah", cari_faktorial )
    