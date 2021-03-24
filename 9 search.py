#Program to find the occurence of any word in a string

def counter(string,search):
    count = 0
    words = string.split()
    for word in words:
        if word == search:
            count += 1
    return count

sentence = input("Please enter a sentence: ")
word = input("Please enter what to search for in the sentence: ")

print(word, "was found", counter(sentence,word), "times.")