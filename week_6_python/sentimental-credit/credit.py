while True:
    try:
        number = int(input("Number: "))
        if number > 0:
            break
    except ValueError:
        print("Please enter a valid card number.")


def invalid():
    print("INVALID")


numberString = str(number)

if len(numberString) not in [13, 15, 16]:
    invalid()

luhnOne = ""
z = -2

while z + (len(numberString)) >= 0:
    luhnOne += str(int(numberString[z]) * 2)
    z -= 2

luhnTwo = 0
for i in range(len(luhnOne)):
    luhnTwo += int(luhnOne[i])

y = -1
while y + (len(numberString)) >= 0:
    luhnTwo += int(numberString[y])
    y -= 2

if str(luhnTwo)[-1] != "0":
    invalid()
elif (numberString[0] == "3" and (numberString[1] == "4" or numberString[1] == "7")) and len(numberString) == 15:
    print("AMEX")
elif (numberString[0] == "5" and (numberString[1] in ["1", "2", "3", "4", "5"])) and len(numberString) == 16:
    print("MASTERCARD")
elif numberString[0] == "4" and (len(numberString) == 13 or len(numberString) == 16):
    print("VISA")
else:
    invalid()
