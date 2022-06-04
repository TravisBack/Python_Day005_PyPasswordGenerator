import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(']
matrix = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letters would you like in your password? "))
numberOfNumbers = int(input("How many numbers would you like? "))
numberOfSymbols = int(input("How many symbols would you like? "))

if numberOfLetters > len(letters):
    print("Number of letters exceeded. Setting number of letters to " + str(len(letters)) + ".")
    numberOfNumbers = len(letters)
if numberOfNumbers > len(numbers):
    print("Number of letters exceeded. Setting number of letters to " + str(len(numbers)) + ".")
    numberOfNumbers = len(numbers)
if numberOfSymbols > len(symbols):
    print("Number of symbols exceeded. Setting number of letters to " + str(len(symbols)) + ".")
    numberOfSymbols = len(symbols)

generatedPassword = ""

while numberOfLetters > 0 or numberOfSymbols > 0 or numberOfNumbers > 0:
    if len(matrix) == 0:
        break

    charType = matrix[random.randint(0, len(matrix) - 1)]
    passwordChar = str(charType[random.randint(0, len(charType) - 1)])

    if charType == letters:
        letters.remove(passwordChar)
        if len(letters) == 0:
            matrix.remove(letters)
        if numberOfLetters > 0:
            numberOfLetters -= 1

    elif charType == numbers:
        numbers.remove(passwordChar)
        if len(numbers) == 0:
            matrix.remove(numbers)
        if numberOfNumbers > 0:
            numberOfNumbers -= 1

    elif charType == symbols:
        symbols.remove(passwordChar)
        if len(symbols) == 0:
            matrix.remove(symbols)
        if numberOfSymbols > 0:
            numberOfSymbols -= 1

    else:
        print("FOOBAR!")

    generatedPassword += passwordChar

print(f"Your generated password is: {generatedPassword}")
