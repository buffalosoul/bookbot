def count_words(text):
    i = 0
    split_text = text.split()
    for word in split_text:
        i += 1
    return i

def character_counter(text):
    lower_case_text = text.lower()
    split_text = lower_case_text.split()
    num_of_characters = {}
    for word in split_text:
        for character in word:
            try:
                if character.lower() in num_of_characters:
                    num_of_characters[character] += 1
                else:
                    num_of_characters[character] = 1
            except:
                print('no character found')
    return num_of_characters

def dictionary_sorter(char_count_dict: dict):
    output_list = []
    char_count_dict.sort()
    for entry in char_count_dict:
        for key in entry:
            if key.isalpha():
                print(f"{key}: {entry[key]}")
            else:
                pass