# Program to search a word in a given string
givenString = open('Text file').read()

toSearch = input('Word to search: ')

if toSearch in givenString:
    print(toSearch,'exists in the string at index',givenString.index(toSearch))
else:
    print('The search phrase does not exist in the string')