# Create a program which accepts user input of a date (yyyy-mm-dd format)
# and prints a customized monthly newsletter header (e.g. "February
# Newsletter", "December: Have you bought all your gifts?") and a fun fact about you

date = input("What is today's date (yyyy-mm-dd)? ")

fun_fact = "I am Batman!"

month = int(date.split('-')[1])
greeting = None

if month == 1:
    greeting = "Greeting 1"
elif month == 2:
    greeting = "Greeting 2"
elif month == 3:
    greeting = "Greeting 3"
elif month == 4:
    greeting = "Greeting 4"
elif month == 5:
    greeting = "Greeting 5"
elif month == 6:
    greeting = "Greeting 6"
elif month == 7:
    greeting = "Greeting 7"
elif month == 8:
    greeting = "Greeting 8"
elif month == 9:
    greeting = "Greeting 9"
elif month == 10:
    greeting = "Greeting 10"
elif month == 11:
    greeting = "Greeting 11"
elif month == 12:
    greeting = "Greeting 12"

print(greeting + ": " + fun_fact)
