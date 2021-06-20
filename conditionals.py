for name in ['Christopher','Susan']:
    print(name)
import sys

brian = open('brian.txt')
print(list(enumerate(brian)))

for nr, line in enumerate(open('brian.txt'), start=1):
   print(nr, line, end="")


user_input = "Cheese"

name = "Cheese" if user_input == "cheese" else "not cheese"

