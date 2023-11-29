import random
#The selection of horses
horses = {"Fidel": {"Speed": 6,"age": 11}, 
          "Castro": {"Speed": 9, "age": 5},
          "Rudalph": {"Speed": 7,"age": 7},
          "Pegasus": {"Speed": 9,"age": 6},
          "Feras": {"Speed": 2,"age": 2},
          }
#creates a list of the horses and then prints the horse names
horse_names = list (horses.keys())
print(f"Horse names: {horse_names}")

#prints atributes of horses
for key, value in horses.items():
  print(f"{key}: {value}")
#Select a horse from the selection 
player_horse_name = input("Select a horse: ")


#if a player does not pick a horse (wrong name) it asks the question again
while player_horse_name not in horse_names:
  print("Please select a valid horse from the list")
  player_horse_name = input("Select a horse: ")

player_horse = horses[player_horse_name]

speed_level = player_horse['Speed']
age = player_horse['age']
#Asks for a bet amount between $5 and $100 and if a different value is said it asks the question again
bet_amount = 0
while bet_amount < 5 or bet_amount > 100:
    bet_amount = int(input("Bet between $5 and $100: "))
    if bet_amount < 5 or bet_amount > 100:
        print("Enter a value between 5 and 100")
  
#asks the player for their name
Player = input("What is your name?: ")
#selects a random winner
def select_random_winner(horses):
  winner = random.choice(list(horses.keys()))
  return winner
#says the winner 
winner = select_random_winner(horses)
print(f"The winner is: {winner}")
#If won, initial bet amount increases 1.5x
if winner == player_horse_name:
  print(f"Congratulations {Player}! You won!")
  print(f"you won: ${int(bet_amount) * 1.5}")
#if lost, it says:
else: 
    print("You lost cuhhhhhh, losserrrr")
