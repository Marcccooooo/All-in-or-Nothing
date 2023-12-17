import random


#random wether for the race 
def get_weather():
  weather_conditions = ["Rain", "Sunny", "Snowy", "Thunder"]
  return random.choice(weather_conditions)



def main():
#The selection of horses

  horses = {
    "Fidel": {"Speed": random.randint(1,10), 
              "age": random.randint(1,10), 
              "Rain": random.randint(1,10), 
              "Sunny": random.randint(1,10),
              "snowy": random.randint(1,10), 
              "thunder": random.randint(1,10)},
    "Castro": {"Speed": random.randint(1,10),
               "age": random.randint(1,10),
               "Rain": random.randint(1,10),
               "Sunny": random.randint(1,10),
               "snowy": random.randint(1,10),
               "thunder": random.randint(1,10)},
    "Rudalph": {"Speed": random.randint(1,10),
                "age": random.randint(1,10),
                "Rain": random.randint(1,10),
                "Sunny": random.randint(1,10),
                "snowy": random.randint(1,10),
                "thunder": random.randint(1,10)},
    "Pegasus": {"Speed": random.randint(1,10),
                "age": random.randint(1,10),
                "Rain": random.randint(1,10),
                "Sunny": random.randint(1,10),
                "snowy": random.randint(1,10),
                "thunder": random.randint(1,10)},
    "Feras": {"Speed": random.randint(1,10),
              "age": random.randint(1,10),
              "Rain": random.randint(1,10),
              "Sunny": random.randint(1,10),
              "snowy": random.randint(1,10),
              "thunder": random.randint(1,10)},
    }

  
  current_weather = get_weather()
  print(f"The weather today is: {current_weather}")
  horse_names = list(horses.keys())
  print(f"Horse names: {horse_names}")
  # Prints attributes of horses
  for key, value in horses.items():
      print(f"{key}: {value}")
  # Ask the user how many players will be playing
  num_players = 0
  while num_players < 1 or num_players > 4:
      num_players_str = input("How many players will be playing? ")
      if num_players_str.isdigit():
          num_players = int(num_players_str)
      else:
          print("Enter a number between one and four.")
  # Players select a horse from the selection
  horse_selection = []
  for i in range(num_players):
      valid_horse = False
      while not valid_horse:
          player_horse_name = input(f"Player {i + 1}, Select a horse: ")
          if player_horse_name in horse_names:
              horse_selection.append(player_horse_name)
              valid_horse = True
          else:
              print("Please select a valid horse from the list")


    # Ask for a bet amount between $5 and $100 for each player 
  bet_amounts = []
  for i in range(num_players):
      bet_amount = 0
      while bet_amount < 5 or bet_amount > 100:
          bet_amount = int(input(f"Player {i + 1}, Please enter a bet amount between $5 and $100: "))
          if bet_amount < 5 or bet_amount > 100:
              print("Enter a value between 5 and 100")
      bet_amounts.append(bet_amount)
  # Select a random winner
  winner = select_random_winner(horses, current_weather)
  print(f"The winner is: {winner}")
  # Check which player is the winner and display the result
  for player, selected_horse in enumerate(horse_selection):
      if selected_horse == winner:
          print(f"Congratulations Player {player + 1}! You won!")
          print(f"You won: ${int(bet_amounts[player]) * 1.5}")
      else:
          print(f"Sorry Player {player + 1}, better luck next time.")

# fucntion that creates a weight for the horses increasing likey hood of horses to win depedning on thier atributes 
def calculate_chances(horses, current_weather, horse_name):
    base_weight = 1.0
    wether_weight = horses[horse_name].get("Weather", {}).get(current_weather, 0)
    speed_weight = horses[horse_name].get("Speed", 0) * 0.1
    age_weight = (4 - abs(horses[horse_name].get("age", 0) - 4)) * 0.1

    total_weight = base_weight + wether_weight + speed_weight + age_weight
    return total_weight

# fucntion that randomly selects a winner from the horeses 
# It takes in the weight of the horses giving some higher chances to win
def select_random_winner(horses, current_weather):
    chances = {horse: calculate_chances(horses, current_weather, horse)
               for horse in horses
               }
    winner = random.choices(list(chances.keys()), weights=list(chances.values()))[0]
    return winner



main()

