from Question import Question

#List of question prompts with answer choices
question_prompts = [
	"What color is Ichigo's Bankai?\n(a) Black & White\n(b) Purple\n(c) Orange\n\n" , 
	"From whom does Luffy get his straw hat from?\n(a) Gold Rodger\n(b) Zoro\n(c) Ace\n(d) Law\n\n",
	"What is Gon's last name?\n(a) Monkey\n(b) Uzumaki\n(c) Freecs\n(d) Jojo\n\n",
	"What is the second Pokemon that Ash Ketchum caught in Sinnoh?\n(a) Turtwig\n(b) Starly\n(c) Chimchar\n(d) Buizel\n\n",
	"How many ninja from Konoha went on to the third stage(after the preliminairies) of the Chunin Exams?\n(a) Three\n(b) Four\n(c) Five\n(d) Six\n\n"
]

#Using the Question class, this creates a Question object with the prompt given as well as the answer
questions = [
	Question(question_prompts[0], "a"),
	Question(question_prompts[1], "a"),
	Question(question_prompts[2], "c"),
	Question(question_prompts[3], "a"),
	Question(question_prompts[4], "c")


]

#Function that runs the game, input a list of questions
def run_test(questions):

	#keep track of score
	score = 0
	#for loop that runs until number of questions run out
	for question in questions:
		#prompts the user to answer the question
		answer = input(question.prompt)
		#if the answer is correct, score gets incremented by 1
		if answer == question.answer:
			score += 1

	#prints out final score 
	print("You got " + str(score) + "/" + str(len(questions)) + " correct!" )


#call the run_test function to run the game
run_test(questions)