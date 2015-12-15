__author__ = 'gauth_000'
dictionary = {}


def add_entry(entry):
    dictionary[entry[0]] = dictionary.get(entry[0], [])
    dictionary[entry[0]].append(entry[1])


def search(word):
    return ', '.join(dictionary[word]) if word in dictionary else word + " doesn't exist"


def synonyms(phrase):
    return ', '.join([k for k, v in dictionary.items() if phrase in v])


def display():
    for k in sorted(dictionary):
        print(k, dictionary[k])


add_entry(('a', 'b'))
add_entry(('b', 'b'))
add_entry(('c', 'd'))
add_entry(('e', 'f'))
add_entry(('c', 'f'))
add_entry(('t', 'f'))
add_entry(('i', 'j'))
display()
print(search('c'))
print(synonyms('f'))