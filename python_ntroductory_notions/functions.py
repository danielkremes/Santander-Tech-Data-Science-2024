# functions

def calculate(operation, number_one, number_two):
    if operation == "+":
        return number_one + number_two
    elif operation == "-":
        return number_one - number_two
    elif operation == "*":
        return number_one * number_two
    elif operation == "/":
        return number_one / number_two
    else:
        print("error")

print(calculate("+",20,20))

def message_user_new(name, course = "python"):
    print(f"Welcome {name}, it's nice too meet you, your are make course about {course}")

print("Your name please !")
name_user = input("")
print("Your course please !")
name_course = input("")

message_user_new(name_user,name_course)

