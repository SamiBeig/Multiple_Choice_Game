from Question import Question

#List of question prompts with answer choices
question_prompts = [
	"What color is Ichigo's Bankai?\n(a) Black & White\n(b) Purple\n(c) Orange\n\n" , 
	"From whom does Luffy get his straw hat from?\n(a) Gold Roger\n(b) Zoro\n(c) Ace\n(d) Law\n\n",
	"What is the name of Killua's father?\n(a) Silva\n(b) Zeno\n(c) Kikyo\n(d) Milluki\n\n",
	"What is the second Pokemon that Ash Ketchum caught in Sinnoh?\n(a) Turtwig\n(b) Starly\n(c) Chimchar\n(d) Buizel\n\n",
	"In Attack on Titan, who was the first member of Levi's squad to be killed by Annie, the Female Titan?\n(a) Eld\n(b) Petra\n(c) Gunther\n(d) Oluo\n\n"
	"How many ninja from Konoha went on to the third stage(after the preliminairies) of the Chunin Exams?\n(a) Three\n(b) Four\n(c) Five\n(d) Six\n\n",
	"What kind of animal was the Chimera Ant who became friends with Killua and helped him?\n(a) Cheetah\n(b) Chameleon\n(c) Octopus\n(d) Bear\n\n",
	"Who is the 8th division captain in Bleach?\n(a) Soifon\n(b) Shinsui Kyoraku\n(c) Sosuke Aizen\n(d) Ichimaru Gin\n\n",
	"In Attack on Titan, Jean and Annie compared Marlo to one person. Who is that person?\n(a) Bertolt\n(b) Armin\n(c) Reiner\n(d) Eren",
	"What Pokemon is exactly before Stantler in the national pokedex?\n(a) Porygon2\n(b) Smeargle\n(c) Phanpy\n(d) Magby\n\n"
]

#Using the Question class, this creates a Question object with the prompt given as well as the answer
questions = [
	Question(question_prompts[0], "a"),
	Question(question_prompts[1], "a"),
	Question(question_prompts[2], "a"),
	Question(question_prompts[3], "a"),
	Question(question_prompts[4], "c").
	Question(question_prompts[5], "c").
	Question(question_prompts[6], "c"),
	Question(question_prompts[7], "b"),
	Question(question_prompts[8], "d"),
	Question(question_prompts[9], "a"),
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