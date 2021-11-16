import random

comp_wins = 0
player_wins = 0
#user choice
def choose_option():
    user_choice = input("Choose Rock,Paper or Scissors: ")
    if user_choice in ["Rock","rock","r","R"]:
        user_choice = "r"
    elif user_choice in ["paper","Paper","p","P"]:
        user_choice = "p"
    elif user_choice in ["Scissors","scissors","S","s"]:
        user_choice = "s"
    else:
        print(" choice invalid,please try again")
        choose_option()
    return user_choice

# computer choice
def computer_option():
      comp_choice = random.randint(1,3)
      if comp_choice == 1:
          comp_choice = "r"
      elif comp_choice == 2:
          comp_choice = "p"
      else:
          comp_choice = "s"
      return comp_choice


while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if user_choice =="r":
        if comp_choice == "r":
            print("both of you choose rock. ITS A TIE !!")
        elif comp_choice =="p":
            print("computer chose paper. YOU LOSE !!")
            comp_wins+=1
        elif comp_choice == "s":
            print("computer chose scissors. YOU WIN !!")
            player_wins+=1
    elif user_choice =="p":
        if comp_choice == "p":
            print("both of you chose paper. ITS A TIE !!")
        elif comp_choice =="s":
            print("computer chose scissors. YOU LOSE !!")
            comp_wins+=1
        elif comp_choice == "r":
            print("computer chose rock. YOU WIN !!")
            player_wins+=1
    elif user_choice =="s":
        if comp_choice == "s":
            print("both of you chose scissors. ITS A TIE !!")
        elif comp_choice =="r":
            print("computer chose rock. YOU LOSE !!")
            comp_wins+=1
        elif comp_choice == "p":
            print("computer chose paper. YOU WIN !!")
            player_wins+=1


    print("")
    print("player wins: "+ str(player_wins))
    print("computer wins: "+ str(comp_wins))
    print("")

    user_choice = input("Do you wannna continue? (y/n) ")

    if user_choice in ["Y","y"]:
        pass
    elif user_choice in ["N","n"]:
        break
    else:
        break












