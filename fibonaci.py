# 2.(B) fungsi rekursif fibonaci
# 1 1 2 3 5 8 13 21 34 55
def fibonaci (n) :
   if n < 1:
       return "angka tidak dapat dihitung"
   elif n==1 or n==2:
       return 1
   else :
       return fibonaci(n-1) + fibonaci(n-2)
a = int(input("masukan nilai n: "))
hasil = fibonaci(a)
print(hasil)
