import math
n = int(input("Masukan nilai n: "))
z = 0

for i in range(1, n + 1): 
  for j in range(i, n + 1): 
    x = i * i + j * j 

    y = int(math.sqrt(x)) 
  
    if (y * y == x and y <= n): 
      z += 1
      print("(",i, j, n,")")    

print(z, "Pasang")
  
  

