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


def write_html_file(new_html):
    """
    writes a string to html file
    :return: None
    """
    file_path = os.path.join(BASE_PATH, 'animals.html')
    try:
        with open(file_path, 'w', encoding='utf-8') as file_obj:
            return file_obj.write(new_html)
    except (json.JSONDecodeError, FileNotFoundError):
        return ""


def print_animals(animals: list):
    """
    Checks if we have the animal data we want to print and prints it.
    If we have no name for the animal, we skip it.
    If any other data is missing, we only skip that data.
    :param animals: list of animal dicts
    :return: a string with all available animal data
    """
    output = ""
    for animal in animals:
        animal_name = animal.get('name')
        animal_locations = animal.get('locations')
        animal_characteristics = animal.get('characteristics', {})
        if animal_name:
            output += (f'<li class="cards__item">\n'
                       f'<div class="card__title">{animal_name}</div>\n')
            animal_characteristics_diet = animal_characteristics.get('diet')
            if animal_characteristics_diet:
                output += (f'<p class="card__text">\n'
                           f'<strong>Diet:</strong> {animal_characteristics_diet}<br/>\n')
            if animal_locations:
                output += f"<strong>Location:</strong> {animal_locations[0]}<br/>\n"
            animal_characteristics_type = animal_characteristics.get('type')
            if animal_characteristics_type:
                output += f"<strong>Type:</strong> {animal_characteristics_type}<br/>\n"
            output += "</p>\n</li>\n"
    return output


def past_animals_in_html(html_template: str, animals_for_html: str):
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
    animals_for_html = print_animals(animals)
    html_template = read_html_file()
    new_html = past_animals_in_html(html_template, animals_for_html)
    write_html_file(new_html)


if __name__ == '__main__':
    main()
