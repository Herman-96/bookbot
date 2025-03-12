def wordCounter(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        numWords = len(file_contents.split())
    return numWords

def get_num_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        num_letters = {}
        for letters in lower_case:
            if letters in num_letters:
                num_letters[letters] += 1
            else:
                num_letters[letters] = 1
    return num_letters

def sort_letters(letter_dict):
    letters_list = []
    for char, count in letter_dict.items():
        if char.isalpha():
            letters_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list
