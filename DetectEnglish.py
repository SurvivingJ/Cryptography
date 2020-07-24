UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + '\t\n' + ' '

def load_dictionary():
    dictionary_file = open('dictionary.txt')
    english_words = {}
    for word in dictionary_file.read().split('\n'):
        english_words[word] = None
    dictionary_file.close()
    return english_words

english_words = load_dictionary()

def remove_non_letters(message):
    letters_only = []
    for ch in message:
        if ch in LETTERS_AND_SPACE:
            letters_only.append(ch)
    return "".join(letters_only)

def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0
    
    matches = 0
    for word in possible_words:
        word = word.lower()
        if word in english_words:
            matches += 1
    return float(matches) / len(possible_words)

def is_english(message, wordPercentage = 20, letterPercentage = 85):
    words_match = get_english_count(message) * 100 >= wordPercentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letterPercentage
    return words_match and letters_match