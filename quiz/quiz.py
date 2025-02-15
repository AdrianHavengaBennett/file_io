def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option

def add_question():
    print("")
    question = input("Enter a question\n")

    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))

    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def ask_questions():
    questions = []
    answers = []

    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()

    for i, text in enumerate(lines):
        if i % 2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0

    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Right!")
            print(score)
        else:
            print("Wrong!")

    print("You answered {0} out of {1} questions correctly.".format(score, number_of_questions))


def game_loop():
    play_game = True
    while play_game:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            print("You selected 'Exit game'\nGood bye!")
            play_game = False
        else:
            print("Invalid option")
        print("")

game_loop()