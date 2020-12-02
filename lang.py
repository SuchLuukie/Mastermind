import os
clear = lambda: os.system('cls')

class Languages(object):
	"""docstring for Languages"""
	def __init__(self, arg):
		self.arg = arg

		if self.arg == "ENG":

			self.firstPlay = "Do you understand the rules of the game?"
			self.notFirstPlay = "Would you like to play again"

			self.userCodeGuess = "Please make your guess. ("
			self.amountColors = ") (4 colors)"

			self.incorrectLength = "Incorrect length (4)"
			self.incorrectColor = "Incorrect color"

			self.correctCode = "You guessed the code correctly!"
			self.outOfGuesses = "You've ran out of guesses, you lost."
			self.codeReveal = "The code was: "

			self.guessesLeft1 = "You have "
			self.guessesLeft2 = " guess(es) left."



		elif self.arg == "NL":

			self.firstPlay = "Begrijp je de regels van het spel?"
			self.notFirstPlay = "Wil je opnieuw spelen?"

			self.userCodeGuess = "Maak een gok. ("
			self.amountColors = ") (4 kleuren)"

			self.incorrectLength = "Onjuiste lengte (4)"
			self.incorrectColor = "Onjuiste kleur"

			self.correctCode = "Je hebt de code geraden!"
			self.outOfGuesses = "Je hebt geen beurten meer, je hebt verloren"
			self.codeReveal = "De code was: "

			self.guessesLeft1 = "Je hebt "
			self.guessesLeft2 = " gok(en) over."

	def displayMenuEng(self):
		clear()
		print("You're about to play Mastermind.")
		print("You play against the computer.")
		print("The computer makes a code of 4 colors long, you may use every color as many times as you'd like.")
		print("You then need to guess the correct code in 12 moves")
		print()
		print("Next to your guess it displays 2 cells.")
		print("If you guess the correct color at the correct position it displays in the left cell by amount")
		print("If you guess the correct color but not the right position it displays it in the right cell by amount")
		print()
		print()
		print("Good luck!")


	def displayMenuNl(self):
		clear()
		print("Je gaat Mastermind spelen.")
		print("Je speelt tegen de computer.")
		print("De computer maakt een code van 4 kleuren lang, je mag een kleur zovaak als je wilt gebruiken.")
		print("Daarna moet je de code correct raden in 12 beurten")
		print()
		print("Naast je gok gaan 2 cellen staan.")
		print("Als je de goede kleur op de goede positie raad, word het in de linkere cell aangegeven.")
		print("Als je de goede kleur maar niet op de juiste positie raad, word het in de rechter cell aangegen.")
		print()
		print()
		print("Veel plezier!")