# pythonLiveProject
This repo will demonstrate live projects in python based on the python experience I got from 100DaysCodingChallenge.

Feel free to share your thought on this project..

# Project
- Coffee making machine
<br>
This project is a console based coffee machine simulator.
It uses OOP as it core Implementation.

### Getting started
open gitbash...clone the project using below line of commands
```bash
    $-> git clone https://github.com/rj80099/pythonLiveProject.git
    $-> cd 001_CoffeeMakingMachine/dist
    $ 001_CoffeeMakingMachine/dist ->./main.exe

````

### Rules
1. To see the report type "report"
2. To exit from app type "off"
3. Only one coffee can be order at a time.
4. User need to select an order from the menu
6. Then insert coins based on the price of your coffee.
7. Order will be sucessfull if the amount is equal/greater then price of your chosen order
8. Remaining change will be given if applicable
5. Resources are upadated on every sucessfull order.
6. You can view profit by typing "report"

- Sake Game 
This is a demo code that was develop using turtle module on a famous snake game.

```bash
    $-> git clone https://github.com/rj80099/pythonLiveProject.git
    $-> cd 002_SnakeGame/dist
    $ 002_SnakeGame/dist ->./main.exe
```

### Rules:
1. Game starts with the snake object at the center of the screen.
2. Player need to move the snake in order to follow food (blue circle).
3. Score will increase on consuming food so as the size of the snake.
4. If the snake hits the wall,the game will restart again.
5. If current score is greater then high score then new high score will be current score.

### Implementation:
1. Snake class in snake.py file inherit from turtle class which define shape and characteristic of a snake
2. Scoreboard class in scoreboard.py file updates score and highscore on screen
3. Food class in food.py file inherit from turtle class which define shape and characteristic of food

