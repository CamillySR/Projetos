# import another_module
#
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")
print(table)


