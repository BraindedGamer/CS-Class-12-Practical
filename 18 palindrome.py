#program to check if the given string is a palindrome

def pali(word):
    reverse = word[::-1]
    return word.lower() == reverse.lower()

print("bye :",pali("bye"))
print("aibohphobia :",pali("aibohphobia"))
print("plaidrome :",pali("plaidrome"))
print("racecar :",pali("racecar"))