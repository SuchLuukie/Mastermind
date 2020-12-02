from random import randint
import os
from clint.textui import colored, puts
from lang import Languages

clear = lambda: os.system('cls')
clear()

colorDict = {
	1: "R",
	2: "G",
	3: "B",
	4: "Y",
	5: "P",
	6: "C"
}

acceptedColor = {
	"R",
	"G",
	"B",
	"Y",
	"P",
	"C"
}

firstPlay = True

def chooseLang():
	global language

	print("ENG/NL?")
	langChoice = input().upper()

	language = Languages(langChoice)
	start()


def start():
	global guesses, totalGuesses, winVar, totalResults, firstPlay

	guesses = 12
	totalGuesses = list()
	totalResults = list()
	winVar = False


	if firstPlay:
		displayMenu()


		print()
		print(language.firstPlay)
		firstPlay = False

	elif not firstPlay:
		print()
		print(language.notFirstPlay)


	userInput = input().lower()

	if userInput == "yes" or userInput == "ja":
		print()
		code = createCode()
		mainFunc(code)

	clear()
	exit()


"""Create code"""
def createCode():
	code = list()
	for i in range(4):
		randomNumber = randint(1, 6)
		
		randomColor = colorDict[randomNumber]
		code.append(randomColor)

	return code


"""Request a guess from the user and make sure it's within the parameters."""
def userCodeGuess():
	print()
	print(language.userCodeGuess, end = " ")

	for a in acceptedColor:
		printCorrectColor(a)
	print(language.amountColors)

	userInput = input().upper()
	userInput = list(userInput)

	#Here it makes sure the guess is 4 long
	if len(userInput) != 4:
		print(language.incorrectLength)
		return False

	#Here it checks if the userInput is in the accepted color dictionary
	for char in userInput:
		if not char in acceptedColor:
			print(language.incorrectColor)
			print()
			return False

	#if that's all true it returns userInput
	return userInput
	


"""Compare the guess to the code, return how many are in the right place and the right color."""
def compareGuessToCode(userGuess, code):
	global winVar

	compareResult = [0, 0]
	oldString = list(userGuess.copy())
	newString = list(userGuess.copy())
	newCode = list(code.copy())

	#If the userGuess is the same as the code the user wins.
	if userGuess == code:
		winVar = True
		return [4, 0]

	#Here it checks if a color is in the same place as code, if so it removes it from newString/Code
	for index in range(0, len(oldString)):
		if oldString[index] == code[index]:
			newString.remove(oldString[index])
			newCode.remove(oldString[index])

			compareResult[0] += 1

	#Here it checks the remaining colors to see if they're in the remaining code
	for index in range(0, len(newString)):
		if newString[index] in newCode:
			#newString.remove(newString[index])
			compareResult[1] += 1

	return compareResult



"""Main function calls the necesarry functions while the user still has guesses"""
def mainFunc(code):
	global guesses

	userGuess = userCodeGuess()
	if userGuess == False:
		mainFunc(code)


	results = compareGuessToCode(userGuess, code)


	if winVar:
		displayFunc(code, results)
		print()
		print(language.correctCode)
		print()
		displayCode(code)
		start()


	if guesses < 1:
		displayFunc(code, results)
		print()
		print(language.outOfGuesses)
		print(language.codeReveal)
		print()
		displayCode(code)
		start()


	if guesses >= 1:
		totalGuesses.append(userGuess)
		totalResults.append(results)

		displayFunc(code, results)
		print(language.guessesLeft1 + str(guesses) + language.guessesLeft2)
		guesses -= 1
		mainFunc(code)



def displayFunc(code, results):
	clear()
	for guess in range(len(totalGuesses)):

		for index in range(len(totalGuesses[guess])):
			print("| ", end ="")
			printCorrectColor(totalGuesses[guess][index])

		print("|", end = "  ")

		for index in range(len(totalResults[guess])):
			print("| " + str(totalResults[guess][index]), end =" ")

		print()

def displayCode(code):
	for index in range(len(code)):
		print("| ", end ="")
		printCorrectColor(code[index])

	print("|")

def displayMenu():
	if language.arg == "ENG":
		language.displayMenuEng()

	elif language.arg == "NL":
		language.displayMenuNl()


def printCorrectColor(color):
	if color == "R":
		print(colored.red('R'), end =" ")

	elif color == "G":
		print(colored.green('G'), end =" ")

	elif color == "B":
		print(colored.blue('B'), end =" ")

	elif color == "Y":
		print(colored.yellow('Y'), end =" ")

	elif color == "P":
		print(colored.magenta('P'), end =" ")

	elif color == "C":
		print(colored.cyan('C'), end =" ")

chooseLang()