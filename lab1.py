def print_menu():
    print("\nMENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")


def execute_menu(user_choice, sample_text):
    if user_choice == 'c':
        print("\nNumber of non-whitespace characters:", get_num_of_non_WS_characters(sample_text))
    elif user_choice == 'w':
        print("\nNumber of words:", get_num_of_words(sample_text))
    elif user_choice == 'f':
        count, edited_text = fix_capitalization(sample_text)
        print(f"Number of letters capitalized: {count}")
        print(f"Edited text: {edited_text}")
    elif user_choice == 'r':
        new_text, exclamation_count, semicolon_count = replace_punctuation(sample_text)
        print("\nPunctuation replaced")
        print("exclamation_count:", exclamation_count)
        print("semicolon_count:", semicolon_count)
        print("Edited text:", new_text)
    elif user_choice == 's':
        new_text = shorten_space(sample_text)
        print("\nShortened spaces:")
        print("Edited text:", new_text)
    elif user_choice == 'q':
        print("\nExiting program.")
        quit()
    else:
        print("\nInvalid option.")


def get_num_of_non_WS_characters(user_text):
    return len([char for char in user_text if not char.isspace()])


def get_num_of_words(user_text):
    return len(user_text.split())


def fix_capitalization(user_text):
    count = 0
    new_text = ""
    sentences = user_text.split(". ")
    for sentence in sentences:
        if len(sentence) > 0:
            if sentence[0].islower():
                count += 1
                new_text += sentence[0].upper() + sentence[1:] + ". "
            else:
                new_text += sentence + ". "
    return count, new_text






def replace_punctuation(user_text):
    exclamation_count = user_text.count('!')
    semicolon_count = user_text.count(';')
    new_text = user_text.replace('!', '.').replace(';', ',')
    return new_text, exclamation_count, semicolon_count


def shorten_space(user_text):
    return ' '.join(user_text.split())


if __name__ == '__main__':
    user_text = input("Enter a sample text: ")
    print("\nYou entered:", user_text)
    while True:
        print_menu()
        user_choice = input("\nChoose an option: ")
        execute_menu(user_choice, user_text)
