# basic robot wars like the vb activity. But could go all out and make it into OOP with a class etc.
# 

import time
import random

#main loop
def robot_wars():
    while True:
        print("Welcome to Robot Wars!")
        time.sleep(2)
        
        # Get robot names - would love to have a list of 5 robots which are based on the robot wars live game.
        robot1 = input("Enter the name of the first robot: ")
        robot2 = input("Enter the name of the second robot: ")
        
        # Initialize energy points. For the better version, I would like to have offence and defense points, special weapons etc. 
        energy1 = 100
        energy2 = 100
        
        # Attack words, could add a few more interesting ones!
        attack_words = ['fires', 'zaps', 'blasts', 'disintegrates', 'demolishes'] 
        
        print("\nBattle Begins!\n")
        time.sleep(1)
        
        # Start the battle - 5 rounds editable.
        for round_num in range(1, 6):
            print(f"Round {round_num}...")
            time.sleep(1)
            
            # Random energy reduction
            damage1 = random.randint(5, 20)
            damage2 = random.randint(5, 20)
            
            energy1 -= damage1
            energy2 -= damage2
            
            attack1 = random.choice(attack_words)
            attack2 = random.choice(attack_words)
            
            # print result to screen
            print(f"{robot1} {attack1} {robot2}, causing {damage1} damage!")
            print(f"{robot2} {attack2} {robot1}, causing {damage2} damage!\n")
            
            time.sleep(2)
            
            # Prevent negative energy display
            energy1 = max(0, energy1)
            energy2 = max(0, energy2)
            
            print(f"{robot1} Energy: {energy1}")
            print(f"{robot2} Energy: {energy2}\n")

            # break if energy is 0
            if energy1 == 0 or energy2 == 0:
                break
        
        # Determine winner
        if energy1 > energy2:
            winner = robot1
        elif energy2 > energy1:
            winner = robot2
        else:
            winner = "It's a tie!"
        
        print("\nFinal Score:")
        print(f"{robot1} Energy: {energy1}")
        print(f"{robot2} Energy: {energy2}")
        
        if winner != "It's a tie!":
            print(f"\n🏆 {winner} WINS the Robot Wars! 🏆")
        else:
            print("\nIt's a tie! Both robots are equally matched!")
        
        # Restart option - Strip to remove any spaces / characters and .lower returns in lower case
        restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thanks for playing Robot Wars!")
            break

# Run the game
robot_wars()
