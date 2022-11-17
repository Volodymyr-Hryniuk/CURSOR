import json


class Plant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def save(self):
        file = open("database/plants.json", "r")
        data_in_json = file.read()
        file.close()
        data = json.loads(data_in_json)
        new_plant = {
            "name": self.name,
            "location": self.location
        }
        data.append(new_plant)
        file = open("database/plants.json", "w")
        file.write(json.dumps(data))
        file.close()

    @staticmethod
    def get_all():
        file = open("database/plants.json", "r")
        plants = json.loads(file.read())
        file.close()
        for plant in plants:
            print(plant["name"])
            print(plant["location"])
