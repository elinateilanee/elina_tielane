#for cikls
'''age = float(input("Ievadiet suņa vecumu:"))

if age <= 2:
    print("Jūsu suns ir", age * 10.5, "gadus vecs suņa gados")
else:
    print("Jūsu suns ir", (age - 2) * 4 + 21, "gadus vecs suņa gados")'''

'''for i in range (1,21):
    print(i ,'autobusa pietura')'''
rinda = 5
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")