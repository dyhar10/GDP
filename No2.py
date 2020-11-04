n = int(input("Masukan banyak bilangan n: "))
a = int(input("Masukan bilangan a: "))
b = int(input("Masukan bilangan b: "))

jumlah = 0
for i in range(0, n, 1):
  if (i % a == 0 or i % b == 0):
    jumlah += i

print(jumlah)
