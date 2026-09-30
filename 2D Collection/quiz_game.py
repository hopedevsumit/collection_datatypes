#quiz game======================


questions = 	("How many element are in the preodic table?: ",
		 "Which animal lays the largest egg?: ",
		 "What is the most abundant gas in earth's atmosphere?: ",
		 "How many bones are in the human body?: ",
		 "Which planet in the solar system is the hottest?: ",)


options = 	(("A. 116 ","B. 117 ","C. 118 ","D. 119 "),
		 ("A. Elephant ","B. Whale ","C. Crocodile ","D. Ortrich "),
		 ("A. Nitrogen ","B. Oxygen ","C. Carbon-dioxide ","D. Hydrogen "),
		 ("A. 206 ","B. 207 ","C. 208 ","D. 209 "),
		 ("A.Mercury ","B. Venus ","C. Earth ","D. Mars "))


answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
	print("-----------------------")
	print(question)

	for option in options[question_num]:
		print(option)
	

	guess = input("Enter (A,B,C,D): ").upper()
	guesses.append(guess)
	if guess == answers[question_num]:
		score += 1
		print("CORRECT!")
	else:
		print("INCCRECT!")
		print(f"{answers[question_num]} IS the correct answer")
	question_num += 1
		