userInput = input("Text: ")
L = 0.0
W = 0.0
S = 0.0

for i in range(len(userInput)):
    if (userInput[i].isalpha()):
        L = L + 1
    if (userInput[i] == " "):
        W = W + 1
    if (userInput[i] in [".", "!", "?"]):
        S = S + 1


W = W + 1

L = (L / W) * 100
S = (S / W) * 100
grade = 0.0588 * L - 0.296 * S - 15.8
finalGrade = int(round(grade))

if (finalGrade < 1):
    print("Before Grade 1")
elif (finalGrade >= 16):
    print("Grade 16+")
else:
    print(f"Grade {finalGrade}")
