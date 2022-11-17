import random


possibleChoose = ["Rock", "Paper", "Scissors"]

usr_points = 0
pc_points = 0


def UserInput():

    while True:
        usr_choose = input("Choose an option:\n1. Rock\n2. Paper\n3. Scissors\n--> ")

        if usr_choose.isdigit():
            usr_choose = int(usr_choose)
            if 0 < usr_choose < 4:
                usr_choose -= 1
                break
            else:
                print("Invalid number, please retry.")
        else:
            print("You should insert a number, please retry.")

    return usr_choose


def PrintChoose(usr_choose):

    print("You have chosen " + possibleChoose[usr_choose])
    pc_choose = random.randint(0, 2)
    print("The computer has chosen " + possibleChoose[pc_choose])
    return pc_choose


def CheckVictory(usr_choose, pc_choose, usr_pt, pc_pt):

    is_tie = False

    if usr_choose == pc_choose:
        print("That's a tie, retry!")
        Game()
        is_tie = True
    elif usr_choose == pc_choose - 1:
        print("Pc won!")
        pc_pt += 1
    else:
        print("You won!")
        usr_pt += 1

    return usr_pt, pc_pt, is_tie


def PrintPoints():

    print(f"Your score: {usr_points}")
    print(f"Computer score: {pc_points}")


def Game():

    global usr_points, pc_points

    USR_choose = UserInput()
    PC_Choose = PrintChoose(USR_choose)
    usr_points, pc_points, is_tie = CheckVictory(USR_choose, PC_Choose, usr_points, pc_points)
    if not is_tie:
        PrintPoints()


def main():

    while True:
        play = input("Welcome to rock, paper, scissors!\nDo you want to play (Yes/No)? ")
        play = play.capitalize()

        if play == "No":
            print("Exiting the game...")
            break
        elif play == "Yes":
            Game()

        else:
            print("Invalid syntax, please retry!")


main()
