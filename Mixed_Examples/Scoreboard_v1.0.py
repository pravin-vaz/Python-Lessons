#This program is a simple scoreboard in console to show team names, scores,etc. 
#In the future, there will be a time function

import os
import time

home_team_name = ''
away_team_name = ''
home_team_score = 0
away_team_score = 0

def display_scoreboard():
    global home_team_score, away_team_score
    os.system('clear')  # For Linux/Mac
    #os.system('cls')  # For Windows
    
    print(f'Score: {home_team_name} {home_team_score} - {away_team_score} {away_team_name}')
      #time.sleep(1)
    #os.system('clear')  # For Linux/Mac
        #os.system('cls')  # For Windows

def add_home_team():
    global home_team_name
    home_team_name = input("Enter the home team name: ")

def add_away_team():
    global away_team_name
    away_team_name = input("Enter the away team name: ")

def edit_home_team():
    global home_team_name
    home_team_name = input("Enter the new home team name: ")

def edit_away_team():
    global away_team_name
    away_team_name = input("Enter the new away team name: ")

def add_home_team_score():
    global home_team_score
    home_team_score += 1

def add_away_team_score():
    global away_team_score
    away_team_score += 1

def subtract_home_team_score():
    global home_team_score
    home_team_score -= 1

def subtract_away_team_score():
    global away_team_score
    away_team_score -= 1

def add_player_score(team):
    player_name = input(f"Enter the {team} player name: ")
    player_score = input(f"Enter the {team} player score: ")
    player_time = input(f"Enter the {team} player time: ")
    print(f"{player_name} ({player_score}) - {player_time}'")

def main():
    while True:
        display_scoreboard()
        print('1. Add home team name')
        print('2. Add away team name')
        print('3. Edit home team name')
        print('4. Edit away team name')
        print('5. Add home team score')
        print('6. Add away team score')
        print('7. Subtract home team score')
        print('8. Subtract away team score')
        print('9. Add player score for home team')
        print('10. Add player score for away team')
        #print('11. Display scoreboard')
        print('12. Quit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            add_home_team()
        elif choice == '2':
            add_away_team()
        elif choice == '3':
            edit_home_team()
        elif choice == '4':
            edit_away_team()
        elif choice == '5':
            add_home_team_score()
        elif choice == '6':
            add_away_team_score()
        elif choice == '7':
            subtract_home_team_score()
        elif choice == '8':
            subtract_away_team_score()
        elif choice == '9':
            add_player_score('home')
        elif choice == '10':
            add_player_score('away')
        # elif choice == '11':
           #display_scoreboard()
        elif choice == '12':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
