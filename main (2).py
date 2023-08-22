#Display title
print(r"""

  .---. .-. .-.,-. _____    _______ ,-.         ,---.   .-.  
 ( .-. \| | | ||(|/___  /  |__   __||(||\    /| | .-'   |  ) 
(_)| | || | | |(_)   / /)    )| |   (_)|(\  / | | `-.   | /  
 | ||\ || | | || |  / /(_)  (_) |   | |(_)\/  | | .-'   |/   
 \ `-\\/| `-')|| | / /___     | |   | || \  / | |  `--. (    
  `---\|`---(_)`-'(_____/     `-'   `-'| |\/| | /( __.'(_)   
                                       '-'  '-'(__)          

""")

#Display quiz rules
print("Welcome to the Capitals Quiz Show! We will ask you some True or False questions regarding locations and their capitals. Please make sure you answer the questions ONLY using the letters T and F (for true and false, respectively).Have fun and share this quiz with your friends!")
print()

#Store at least 3 questions in a tuple
questions = ('1. Sydney is the capital of Australia.', '2. Rio de Janeiro is the capital of Brazil.', '3. Tokyo is the capital of Japan.', '4. Havana is the capital of Cuba.', '5. Niamey is the capital of Niger.')

#Store each question's respective answer
answers = ('F', 'F', 'T', 'T','T')

#Start counter variable outside of loop
countRight = 0

#Calculate number of questions
questionNumber = len(questions)

#Loop through tuple to display each question to the user
for question in range(questionNumber):
  #Print out question
  print(questions[question])

  #Prompt user for answer and validate input
  guess = "Y"

  while ((guess != "T") and (guess != "F")):
    guess = input("Please enter 'T' for true or 'F' for false: ")
    print()

  #Compare user guess to correct answer
  if(guess == answers[question]):
    countRight += 1

#Print out final score to user.
print (f"You got {countRight} out of {questionNumber} correct. Thanks for playing!")
    
