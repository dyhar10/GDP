#Belum selesai

x = ""
n = int(input("Masukan banyak kata yang dialarang: "))

for i in range(n):
  x[i] = input("Masukan kata yang dilarang: ")

w = input("Masukan kata yang akan diganti: ")

for i in range(n):
  print (x[i])

print(w)