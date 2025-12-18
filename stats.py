def get_num_words(book):
    words = book.split()
    counter = 0 
    for word in words:
        counter +=1
    return counter
def get_num_chars(book):
    text = book
    my_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
    'y': 0, 'z': 0,
    '!': 0, '"': 0, '#': 0, '$': 0, '%': 0, '&': 0,
    "'": 0, '(': 0, ')': 0, '*': 0, '+': 0, ',': 0,
    '-': 0, '.': 0, '/': 0, ':': 0, ';': 0, '<': 0,
    '=': 0, '>': 0, '?': 0, '@': 0, '[': 0, '\\': 0,
    ']': 0, '^': 0, '_': 0, '{': 0, '|': 0, '}': 0,
    '~': 0
    }      
    for letter in text.lower():
        if letter in my_dict:
            my_dict[letter] += 1
    return my_dict
def sorted_dictionary(diction):
    result = []
    for char, num in sorted(diction.items(), key=lambda x: x[1], reverse=True):
        if char.isalpha():
            result.append({char: num})
    return result
