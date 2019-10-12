import random
user_score = 0
comp_score = 0

print("""1-Rock
         2-Paper
         3-Scissors""")

choices ={'1':"rock",'2':"paper",'3':"scissors"}

i = 0
while i <=10:
    p_choice = input("Enter your choice 1,2,3\n")

    user_choice = choices[p_choice]
    comp_choice = random.choice(['rock','paper','scissors'])  

    if user_choice == "rock" :

        if comp_choice == "scissors":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("You win!!!!")
            
        elif comp_choice == "paper":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("computer wins!!!")
            
        else:
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("it's a draw!")
        
    elif user_choice == "scissors":

        if comp_choice == "rock":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("Computer's better!!")
        
        elif comp_choice == "paper":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("winner!!!")
        
        else:
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("It's a draw!")
         
    else:
        if comp_choice == "rock":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("You rock!!!")
        
        elif comp_choice == "scissors":
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("Bad luck!!!")
        
        else:
            print(f'you:{user_choice}')
            print(f'comp:{comp_choice}')
            print("it's a draw!")
    input("To play again press Enter,To quit press 'ctrl+z'")
    i+=1
