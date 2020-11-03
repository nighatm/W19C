def addTwo(numberOne, numberTwo):
    result =  numberOne + numberTwo
    return numberOne + numberTwo
print(addTwo(5,3))

# if x is larger than 10, print to the terminal "That is a large number!"
# else if x is equal to 10, print to the terminal "That is the number 10!"
# otherwise, print to the terminal "That is a small number!"
x=15
if x > 10:
    print("That's a large number!")
elif x ==10:
    print("That's the number 10!")
elif x<10:
    print("That's a small number!")

    fruits = ["apple", "orange", "grapes"]

cool_list = [1,2,3,4]

for number in cool_list:

    print(number)

class TweeterUser:
    def __init__(self, age, name, address):
        self.age = age
        self.name = name
        self.address = address
