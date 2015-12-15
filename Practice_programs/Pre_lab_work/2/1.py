__author__ = 'gauth_000'

dictionary = {}


def add(words):
    dictionary[words[0]] = words[1]


def search(word):
    if word in dictionary:
        return dictionary[word]


def synonyms(meaning):
    words = []
    for k, v in dictionary.items():
        if meaning == v:
            words.append(k)
    return words


def delete(word):
    if word in dictionary:
        del dictionary[word]


def display_words():
    if dictionary:
        print('\n'.join(sorted(dictionary)))
    else:
        print('Dictionary is empty')


choice = -1
while choice != 'q':
    print('\t\t\t\t\t\t\t\tMenu',
          '\t\t\t\t\t\t\t\t1 - Add a word to the dictionary',
          '\t\t\t\t\t\t\t\t2 - Look up a word',
          '\t\t\t\t\t\t\t\t3 - Synonyms',
          '\t\t\t\t\t\t\t\t4 - Delete a word',
          '\t\t\t\t\t\t\t\t5 - Display words',
          '\t\t\t\t\t\t\t\tq - Quit',
          sep='\n')
    choice = input()
    if choice == '1':
        add(str(input('Use the format <word>:<meaning>\n')).strip().split(':'))
    elif choice == '2':
        meaning = search(input())
        if meaning:
            print('Meaning :', meaning)
        else:
            print('Word not found')
    elif choice == '3':
        meaning = synonyms(input())
        if meaning:
            print('Synonyms are ', ', '.join(meaning))
        else:
            print('Synonyms not found')
    elif choice == '4':
        word = input()
        if word in dictionary:
            delete(word)
            print('Word deleted')
        else:
            print('Word not found')
    elif choice == '5':
        display_words()
