import pandas
import turtle

#screen
screen = turtle.Screen()
screen.screensize(canvwidth=677, canvheight=580)
image = "countries_of_europe.gif"
screen.addshape(image)
turtle.shape(image)

#data in panda
data = pandas.read_csv("countries_of_eu.csv")
all_countries = data.name.to_list()
guessed_countries = []

#ask user




while len(guessed_countries) < 44:
    answer_user = screen.textinput(title=f"{len(guessed_countries)}/44 Countries in Europe Correct", prompt="Can you name the countries of Europe?").title()

    if answer_user == "Exit":
        break

    if answer_user in all_countries:
        guessed_countries.append(answer_user)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("green")
        t.penup()
        country_data = data[data.name == answer_user]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer_user)










# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()