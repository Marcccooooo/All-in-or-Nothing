## Description
#### The code is used as a game for others. It is a luck-based game where you are able to pick one horse out of a few selections and each one has unique and different attributes. It is nothing more than entertainment and a quick game of horse racing.

## Summary
#### When the code is run, you are presented with a list of horses with each one's name, age, and speed. After selecting the horse, you are to bet an amount of money between $5 and $100. Then you must enter your name to start the race. If lost, you win no extra money and you are presented with the real winner and a prompt saying you lost. However, if won then you are told congratulations, and you are presented with the amount of money you have won. 1.5x your initial bet. 

[Link to video of code running](https://drive.google.com/file/d/11aUQOQlMiOtCOYKc5IGxllsVCXrzIzku/view)

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



