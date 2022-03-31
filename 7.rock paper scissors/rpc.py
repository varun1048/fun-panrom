from  random import choice
import os
os.system("cls")

rules  = (f""" 
          rules
-> 3 points to win
-> Keys Used 

    Rock        = r
    Paper       = p
    scissors    = s
    
      """)

print("Rock Paper scissors game")
print(rules)
player = input("Enter your name :") 
# player = "varun"
os.system("cls")

score = {
    player :0,
    "computer" :0  
}

# print(score)


inputs  = ['r','p','s']

def increment(player,computer)->True:
    # if (player == 'p' and computer == 'r') or   (player == 's' and computer == 'p') or (player == 'r' and computer == 's'):
    if( ( player == "s") and ( computer == "p")) or (( player == "p") and ( computer == "r")) or (( player == "r") and ( computer == "s")):    
        return True
    return False

def winner(name)->None:
    print(f"""
        {score}
        Game over 
        winner {name}
        
      """)


while True:
    
    print(f"Score Board {score}")
    
    computer_choice = choice(['s','p','r'])
    # print(f"----------{computer_choice}")
    player_choice = input(f"Enter {player}\t:")
    os.system("cls")
    if player_choice in inputs:
        
        
        print(f"\t{player_choice} ----- {player}")
        print(f"\t{computer_choice} ----- Computer")
        if player_choice == computer_choice:
            print("\t\t____________________tie \n")
            
        # print(score[player] = 1  if increment(player_choice,computer_choice) else score['computer'] += 1)
        else:
            if increment(player_choice,computer_choice):
                score[player] +=1
                print(f"\t\t____________________ {player} wins \n")
                
            else:
                
                score["computer"] +=1 
                print("\t\t____________________ computer wins \n")
            
            if score["computer"] == 3 :
                winner("computer")
                break
            if score[player] == 3:
                winner(player)
                break
         
        
    else:
        os.system("cls")
        print(f"invaled input {player}  ' {player_choice} '")
        print(rules)
