import csv
import unidecode

def wordList(filename):
    with open(filename, encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        flat_list = list(reader)
        return [item for sublist in flat_list for item in sublist]

def remove_accents(stringList):
    list = []
    i = 0
    while i < len(stringList):
        list.append(unidecode.unidecode(stringList[i]))
        i += 1
    for i in range(len(list)):
        list[i] = list[i].lower()
    return list

english_4 = wordList('4_letters_english.csv')
english_5 = wordList('5_letters_english.csv')
english_6 = wordList('6_letters_english.csv')
spanish_4 = wordList('4_letters_spanish.csv')
spanish_5 = wordList('5_letters_spanish.csv')
spanish_6 = wordList('6_letters_spanish.csv')
french_4 = wordList('4_letters_french.csv')
french_5 = wordList('5_letters_french.csv')
french_6 = wordList('6_letters_french.csv')

# Final wordlists for all the languages
english_four = remove_accents(english_4)
english_five = remove_accents(english_5)
english_six = remove_accents(english_6)
french_four = remove_accents(french_4)
french_five = remove_accents(french_5)
french_six = remove_accents(french_6)
spanish_four = remove_accents(spanish_4)
spanish_five = remove_accents(spanish_5)
spanish_six = remove_accents(spanish_6)






