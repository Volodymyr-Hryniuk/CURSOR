from models.models import Plant

while True:
    print("1. Add new plant \n"
          "2. Get all plants")
    flag = int(input("Choose:"))
    if flag == 1:
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all()

