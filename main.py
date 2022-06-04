import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(']

matrix = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")

numberOfLetters = int(input("How many letters would you like in your password? "))
numberOfSymbols = int(input("How many symbols would you like? "))
numberOfNumbers = int(input("How many numbers would you like? "))

generatedPassword = ""


while numberOfLetters > 0 or numberOfSymbols > 0 or numberOfNumbers > 0:
    charType = matrix[random.randint(0, len(matrix) - 1)]
    passwordChar = str(charType[random.randint(0, len(charType) - 1)])

    if charType == letters:
        if numberOfLetters > 0:
            numberOfLetters -= 1
        else:
            matrix.remove(letters)
            continue
    elif charType == numbers:
        if numberOfNumbers > 0:
            numberOfNumbers -= 1
        else:
            matrix.remove(numbers)
            continue
    elif charType == symbols:
        if numberOfSymbols > 0:
            numberOfSymbols -= 1
        else:
            matrix.remove(symbols)
            continue
    else:
        print("FOOBAR!")

    generatedPassword += passwordChar

print(generatedPassword)
