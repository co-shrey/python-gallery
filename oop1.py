'''from turtle import Turtle,Screen
t=Turtle()
print(t)
t.shape("turtle")
t.forward(100.00)
my_s=Screen()
print(my_s.canvheight)
my_s.exitonclick()'''
from prettytable import PrettyTable
table=PrettyTable()
#table.field_names=["pokymon","type"]
#table.add_row(["asa","jj"])
table.add_column("name",["shreya","dog"])
table.add_column("age",["12","13"])
table.align="r"
print(table)