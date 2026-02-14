import json
import os


BASE_PATH = os.path.dirname(__file__)


def read_json_file():
    """
    Reads json file and returns list of animals
    :return: Animals data from json file if error empty list
    """
    file_path = os.path.join(BASE_PATH, 'animals_data.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            return json.load(file_obj)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def read_html_file():
    """
    Reads template html file
    :return: html template from html file if error empty string
    """
    file_path = os.path.join(BASE_PATH, 'animals_template.html')
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            return file_obj.read()
    except (json.JSONDecodeError, FileNotFoundError):
        return ""


def write_html_file(new_html: str):
    """
    writes a string to html file
    :return: None
    """
    file_path = os.path.join(BASE_PATH, 'animals.html')
    with open(file_path, 'w', encoding='utf-8') as file_obj:
        file_obj.write(new_html)


def get_animals_for_html(animals: list):
    """
    Checks if we have the animal data we want to print and prints it.
    If we have no name for the animal, we skip it.
    If any other data is missing, we only skip that data.
    :param animals: list of animal dicts
    :return: a string with all available animal data
    """
    output = ""
    for animal_obj in animals:
        output += serialize_animal(animal_obj)
    return output


def serialize_animal(animal_obj: dict):
    """
    Enrich animal data with HTML structure
    :param animal_obj: data for one animal
    :return: serialize animal data as a string
    """
    animal_name = animal_obj.get('name')
    output = ""

    # fail fast if we have no name
    if not animal_name:
        return output

    # structure html elements
    output += (f'<li class="cards__item">\n'
               f'<div class="card__title">{animal_name}</div>\n'
               f'<div class="card__text">\n<ul>\n')
    locations = animal_obj.get('locations')
    if locations:
        output += f'<li><strong>Location:</strong> {locations[0]}</li>\n'

    # serialize animal characteristics
    animal_characteristics = animal_obj.get('characteristics', {})
    output += serialize_animal_characteristics(animal_characteristics)
    output += "</ul>\n</div>\n</li>\n"
    return output


def serialize_animal_characteristics(animal_characteristics):
    """
    Enrich animal data with HTML structure
    :param animal_characteristics: characteristics from animal
    :return: serialize animal characteristics data as a string
    """
    output = ""
    if not animal_characteristics:
        return output
    card_text = {
        'Diet': animal_characteristics.get('diet'),
        'Type': animal_characteristics.get('type'),
        'Lifespan': animal_characteristics.get('lifespan'),
        'Color': animal_characteristics.get('color')
    }
    for label, value in card_text.items():
        if value:
            output += f'<li><strong>{label}:</strong> {value}</li>\n'
    return output


def paste_animals_in_html(html_template: str, animals_for_html: str):
    """
    Combine the html template and animals data into one html file.
    Only if html template contains '__REPLACE_ANIMALS_INFO__' else we get an empty string.
    :param html_template: html template with '__REPLACE_ANIMALS_INFO__' to be replaced
    :param animals_for_html: animals data from html template
    :return: string that combine html_template and animals_for_html or empty string
    """
    if '__REPLACE_ANIMALS_INFO__' not in html_template:
        return ""
    html_template = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_for_html)
    return html_template


def main():
    """
    Main function
    :return: None
    """
    animals = read_json_file()
    animals_for_html = get_animals_for_html(animals)
    html_template = read_html_file()
    new_html = paste_animals_in_html(html_template, animals_for_html)
    write_html_file(new_html)


if __name__ == '__main__':
    main()
