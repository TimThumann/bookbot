
path_to_file = "./books/frankenstein.txt"

def get_text(path):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1


    characters_filtered = {}
    for character in character_counts:
        if character.isalpha():
            characters_filtered[character] = character_counts[character]

    return characters_filtered

def print_report(path):

    number_of_words = count_words(get_text(path))
    character_dict = count_unique_characters(get_text(path))
    character_list = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"--- Begin report of {path} ---")

    print(f"{number_of_words} words found in the document")
    print()

    for character, count in character_list:
        print(f"The '{character}' character was found {count} times")

    print(f"--- End report ---")


if __name__ == "__main__":
    #print(get_text(path_to_file))
    #print(count_words(get_text(path_to_file)))
    #print(count_unique_characters(get_text(path_to_file)))
    print_report(path_to_file)

