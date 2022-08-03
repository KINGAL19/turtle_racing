import random
from turtle import Turtle, Screen

screen = Screen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen.setup(width=500, height=400)
player_list = []
winner_color = None

bet = screen.textinput('Make your bet', f'choose your color: {colors}')

for i in range(6):
    player = Turtle()
    player.shape('turtle')
    player.penup()
    color = random.choice(colors)
    player.color(color)
    colors.remove(color)
    player.goto(-230, -100 + i * 40)
    player_list.append(player)

is_on = True

while is_on:
    for i in player_list:
        i.forward(random.randint(1, 20))
        x, y = i.position()
        if x >= 250:
            is_on = False
            winner_color = i.color()[0]
            break
print(f'Winner is {winner_color}')
if bet == winner_color:
    print('You Win')
else:
    print('You Lose')
screen.exitonclick()
