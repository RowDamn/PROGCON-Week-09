colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

guess = input("Guess a color of the rainbow (lowercase): ").strip().lower()
found = False

for color in colors:
    if guess == color:
        found = True
        break

if found:
    print("Correct! That color is in the rainbow.")
else:
    print("That color is not in the rainbow list.")

print("Rainbow colors:", ", ".join(colors))
