import os
os.system('cls')

Lx =[1,3,4,2,3,8,7]
Ly =[3,2,1,1,2,8,9]

print (f"{set(Lx)& (set(Ly))}")
print (f"{set(Lx).difference (set(Ly))}")
print (f"{set(Ly).difference (set(Lx))}")
print (f"{set(Lx).symmetric_difference (set(Ly))}")
print (f"{set(Lx)|set(Ly)}")