import re


def read_template(template_file):
    """
    Reads in a template file for the madlib game and returns it as a string.
    :param template_file:
    :return:
    """
    try:
        with open(template_file) as f:
            new_template = f.read()
    except FileNotFoundError as file_not_found_error:
        raise file_not_found_error
    else:
        return new_template


def parse_template(new_template):
    """
    Takes a string, returns a stripped template and a tuple of the parts of speech from the curly braces in the string.
    :param new_template:
    :return:
    """
    new_stripped = re.sub(r'\{[^}]*}', '{}', new_template)
    sub_parts = re.findall(r'\{.*?}', new_template)
    return_parts = tuple([word.replace('{', '').replace('}', '') for word in sub_parts])
    return new_stripped, return_parts


def merge(template_str, user_parts):
    """
    Takes a template string and a tuple of madlib words and merges them together.
    param template_str, parts:
    :return:
    """
    user_parts = ['blank' if part == '' else part for part in user_parts]
    merged = template_str.format(*user_parts)
    return merged


print('''
Welcome to the madlib game! What wacky stories will you create today?
''')

template = read_template('../assets/video_game.txt')

stripped, parts = parse_template(template)

new_parts = []

for word in parts:
    new_word = input(f"Enter a {word}. ")
    new_parts.append(new_word)

print(new_parts)
madlib = merge(stripped, new_parts)

with open('../assets/new_file.txt', 'w') as file:
    file.write(madlib)

print(f'Your madlib is: {madlib}')
