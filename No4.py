a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))
c = int(input("Masukan nilai c: "))

if(a != 0 and b!=0):
  c = a+b
  print(c)

if(a == 0 and b!=0):
  a = c-b
  print(a)

if(a != 0 and b==0):
  b = c-a
  print(b)
