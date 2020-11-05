x = int(input("Masukan bilangan n: "))
i = 0
j = 1 
y = x**2 + 1
z = 0
for i in range(y):
  for j in range(y):
    z = i+j
    if(z == y and j > i):
      print("{",i,",",j,"}", end=' ')