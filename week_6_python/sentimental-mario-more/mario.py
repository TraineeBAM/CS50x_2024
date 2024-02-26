x = " "
y = "#"

while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        print("Please enter a valid integer.")

for i in range(height):
    print((x * (height - i - 1)) + (y * (i+1)) + (x*2) + (y * (i+1)))
