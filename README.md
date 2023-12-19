## Description
#### The code is used as a game for others. It is a luck-based game where you are able to pick one horse out of a few selections and each one has unique and different attributes. It is nothing more than entertainment and a quick game of horse racing.
# V1
## Summary
#### When the code is run, you are presented with a list of horses with each one's name, age, and speed. After selecting the horse, you are to bet an amount of money between $5 and $100. Then you must enter your name to start the race. If lost, you win no extra money and you are presented with the real winner and a prompt saying you lost. However, if won then you are told congratulations, and you are presented with the amount of money you have won. 1.5x your initial bet. 

[Link to video of code running V1](https://drive.google.com/file/d/11aUQOQlMiOtCOYKc5IGxllsVCXrzIzku/view)

## Breakthrough Moment

#### 	One thing that was new to us when coding this project was the dictionary and key. It was all new to us however we overcame it and it worked. We used it in order to give all the horses different attributes of speed age and names and later have this dictionary print when run. 
### The selection of horses
#### horses = {"Fidel": {"Speed": 6,"age": 11}, 
####          "Castro": {"Speed": 9, "age": 5},
####          "Rudalph": {"Speed": 7,"age": 7},
####          "Pegasus": {"Speed": 9,"age": 6},
####          "Feras": {"Speed": 2,"age": 2},
####          }
#### horse_names = list (horses.keys())
#### print(f"Horse names: {horse_names}")
#### for key, value in horses.items():
#### print(f"{key}: {value}")


# V2

## Summarize the program's functionality (what does it do?) and purpose (why does it exist and who is it for?)
#### The function of this program is to be a way to bet on horse races. You have a variety of horses to choose from and bet an amount of money from 5-100 dollars. Each race the horses' speed and age change, and the weather is specified for the race changes as well. This program was made for people who like to do horse bets, and win money. If your horse wins, a certain multiplier is added to your bet, however, if you don't get first, you lose. Also, if your input for the horse is wrong or the bet amount the code will ask for another input, or if you don't input a number between 1 and 4 for players the code will handle the error. The code also weights each horse if the speed is higher for the horse it has high-speed weight. If the age of the horse is closer to 4 it has high age weight. If the wether that matches with the current wether is closer to 10 it has a high wether weight. Then it adds all these to the total weight and the code randomizes this taking into account the weight so a higher weight gives more chance to win. But low weight can still win. Players can select the same horse
 [Link to video of code running V2](https://drive.google.com/file/d/11jVk0XJk8K1-XpItTizpwyCN53qPTt5b/view?usp=drive_link)
##  A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new or independently overcame being stuck

#### One breakthrough moment we had during our code was making multiple players eligible to play at once. We later solved this issue by asking for help and seeking assistance. However, it was still difficult because we had to adjust the ways it was done for it to fit our code and keep the style of the code the same as it was. This was our breakthrough moment because multiple times we were not able to add multiple players and we kept encountering errors. 

### this is seen here:  num_players = 0
  ### while num_players < 1 or num_players > 4:
  ### num_players_str = input("How many players will be playing? ")
  ### if num_players_str.isdigit():
  ### num_players = int(num_players_str)
  
  #### This function is then later repeated in each function using this: for i in range(num_players):





