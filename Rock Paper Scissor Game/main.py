def rock_paper_scissor():


    import random
    human_choice = int(input("Enter your choice\n"))

    if (human_choice<1 or human_choice>3):
        human_choice = int(input("Please enter a vaild input\n"))

    comput_choice = random.randint(1,3)

    if (human_choice == 1):
        human_choice_name = "Rock"

    if (human_choice == 2):
        human_choice_name = "Paper"

    if (human_choice == 3):
        human_choice_name = "Scissors"

    if (comput_choice == 1):
        comput_choice_name = "Rock"

    if (comput_choice == 2):
        comput_choice_name = "Paper"

    if (comput_choice == 3):
        comput_choice_name = "Scissors"


    print(f"Your choice = {human_choice_name}\nComputer's choice = {comput_choice_name}")
    if (human_choice== 1 and comput_choice==3 or 
    human_choice== 2 and comput_choice==1 or 
    human_choice== 3 and comput_choice==2):
        print('Human Wins!')

    elif (human_choice== 1 and comput_choice==2 or 
    human_choice== 2 and comput_choice==3 or 
    human_choice== 3 and comput_choice==1):
        
        print("Computer Wins!")

    else:
        print("Its a draw")



name = input("Hey! What's your name?\n")
print(f"Hello {name}! Welcome to this shitty game knowns as Rock Paper Scissor.\nSince you're a noob so I'll explain the rules to you\n\nRules are:\n\tRock vs Paper = Paper wins\n\tRock vs Scissor = Scissor wins\n\tScissor vs Paper = Scissor wins\n")
print(f"{name}, I hope a noobo like you has understood the game now!")
print(f"{name}, Please choose:\n1 for Rock\n2 for paper\n3 for scissor\n")

rock_paper_scissor()