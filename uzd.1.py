print("Hello World")

#uz ekrana izdrukat visus nepara skaitlus no lieotaja ievatida diapozna
jautajums = int(input("Sakums:"))
jautajums2 = int(input("Beigas:"))

for skaitlis in range(jautajums,jautajums2):
    if skaitlis%2 !=0:
        print(skaitlis)

