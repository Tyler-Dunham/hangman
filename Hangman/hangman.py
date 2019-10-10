import random

with open('words.txt', 'r') as f:
	words = f.read().splitlines()

guessed_letters = []

#user chooses difficulty of word
difficulty = input("Easy (3-5), Medium (6-8), or Hard (9-14)?: ")

#easy 3-5
if difficulty == "Easy":
	random_word = random.choice([word for word in words if len(word) <= 5]).upper()

#medium 6-8
if difficulty == "Medium":
	random_word = random.choice([word for word in words if 6 <= len(word) and len(word) <=8]).upper()

#hard 9-14
if difficulty == "Hard":
	random_word = random.choice([word for word in words if 9<= len(word) and len(word) <=14]).upper()

# num of chars in word
print("Your word is " + str(len(random_word)) + " letters long")

# num of blanks
blanks = "_ " * len(random_word)
print(blanks)

# tries, guess, and mistakes
tries = len(random_word) + 4
mistakes = 0 
guess_num = 0 #used for user input 

#display rules
#guess system
#guess = input
#if guess is not in random.word add 1 to mistakes 
#when mistakes == 5 print "you lose" then quit the program
#if guess is in random.word print "_ " * len(random.word) again but with letter filled in 
#when guess == tries: print "you lose" then quit program
#EDITS
#need to do something with multiple of the same letter in a word ex: EagEr
#when full word is guessed print "you win"
#paper system ex: a is guessed and is 3rd in word print _ _ a _

#paper function (work in progress)
def paper():
	for i, letter in enumerate(random_word):
		print(f'{letter if letter in guessed_letters else "_"} {i + 1}')


print("You have " + str(tries) + " tries and up to 5 mistakes")
print("Use all caps for this game! Have Fun! You can guess the word at any time!")

#guessing system
#formatting
while guess_num <= tries:
	guess = input("Guess #" + str(guess_num + 1) + ": ") #guess input
	guess_num += 1

	#if guess word is correct
	if guess == random_word:
		print("You Guessed the word! You win!")
		quit()

	#quit whenever
	if guess == "Quit":
		quit()
	
	#guess right 
	if guess in random_word:
		print("You have found a letter!")
		print(" ")
		guessed_letters.append(guess.capitalize())
		
		paper()

		print("--------------------------------------------------")

	#if guess was wrong
	else:
		print("That letter is not in the word!")

		
		mistakes += 1
		
		print("Mistakes made: " + str(mistakes) + "/5")
		
		print("--------------------------------------------------")
		
		if mistakes == 5:
			print("You lose!")
			print("The word was " + str(random_word))
			quit()