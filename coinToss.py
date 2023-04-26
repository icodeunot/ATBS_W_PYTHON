import random

flipped = []
flippedN = 0
streak = 0
numberOfStreaks = 0

for experimentNumber in range(10000):

    ct = random.randint(0, 1)
    if ct % 2 == 0:
        flipped.append('H')
        print(flipped[flippedN], "Index #:", flippedN)
        if ((len(flipped) > 1) & (flipped[flippedN - 1] == flipped[flippedN])):
            streak += 1
            print("Streak of:", streak)
            if streak == 5:
                numberOfStreaks += 1
                print("Streak of 6 for H! numberOfStreaks:", numberOfStreaks)
                streak = 0
        else:
            streak = 0
        flippedN += 1
    else:
        flipped.append('T')
        print(flipped[flippedN], "Index #:", flippedN)
        if ((len(flipped) > 1) & (flipped[flippedN - 1] == flipped[flippedN])):
            streak += 1
            print("Streak of:", streak)
            if streak == 5:
                numberOfStreaks += 1
                print("Streak of 6 for T! numberOfStreaks:", numberOfStreaks)
                streak = 0
        else:
            streak = 0
        flippedN += 1

print(flippedN, "Counter check")
print(len(flipped), "Flips listed")

print("Chance of streak: %s%%" % (numberOfStreaks / 100))
