import datetime

def get_current_year():
    now = datetime.datetime.now()
    return now.year

def save_to_file(filename, data):
    try:
        with open(filename, 'w',encoding='utf8') as file:
            for car in data:
                file.write("Mašīnas nosaukums: " + car["nosaukums"] + "\n")
                file.write("Gads: " + car["gads"] + "\n")
                file.write("Modelis: " + car["modelis"] + "\n")
                file.write("Cena: " + car["cena"] + "\n\n")
        print("Dati ir veiksmīgi ierakstīti failā", filename)
    except Exception as e:
        print("Kļūda ierakstot failā:", e)


num_cars = int(input("Cik mašīnu informāciju vēlaties ievadīt? "))
current_year = get_current_year()
cars = []
for i in range(num_cars):
    print("\nIevadiet informāciju par", i+1, ". mašīnu:")
    nosaukums = input("Mašīnas nosaukums: ")
    gads = input("Gads: ")
    while not gads.isdigit() or int(gads) > current_year:
        print("Kļūda! Ievadītais gads ir nepareizs. Lūdzu, ievadiet pareizu gadu.")
        gads = input("Gads: ")
    modelis = input("Modelis: ")
    cena = input("Cena: ")
    cars.append({"nosaukums": nosaukums, "gads": gads, "modelis": modelis, "cena": cena})

for car in cars:
    filename = car["nosaukums"] + ".txt"
    save_to_file(filename, [car])