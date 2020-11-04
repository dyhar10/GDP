#belum selesai

n = int(input("Masukan nilai n: "))
temp, a, b, c = 0,0,1,0
n = n**2

for i in range(n):
  temp = a + b
  a = b
  b = temp

  print(a,b,temp)

