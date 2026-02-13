import json
import os


BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_PATH, 'animals_data.json')


def read_json_file():
    """
    Reads json file and returns list of animals
    :return: Animals data from json file if error empty dict
    """
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file_obj:
            return json.load(file_obj)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def print_animals(animals):
    """
    Checks if we have the animal data we want to print and prints it.
    If we have no name for the animal, we skip it.
    If any other data is missing, we only skip that data.
    :param animals:
    :return:
    """
    for animal in animals:
        animal_name = animal.get('name')
        animal_locations = animal.get('locations')
        animal_characteristics = animal.get('characteristics', {})
        if animal_name:
            print(f"Name: {animal_name}")
            animal_characteristics_diet = animal_characteristics.get('diet')
            if animal_characteristics_diet:
                print(f"Diet: {animal_characteristics_diet}")
            if animal_locations:
                print(f"Locations: {animal_locations[0]}")
            animal_characteristics_type = animal_characteristics.get('type')
            if animal_characteristics_type:
                print(f"Type: {animal_characteristics_type}")
            print("-" * 20)



#   Name
#   Ernährung
#   Den ersten Ort aus der Liste locations
#   Typ



def main():
    """
    Main function
    :return: None
    """
    animals = read_json_file()
    print_animals(animals)


if __name__ == '__main__':
    main()
