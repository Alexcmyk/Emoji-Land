import random
from termcolor import colored
from noise import pnoise2

def generate_land(rows=10, cols=10):
    data = [" ", ".","-", "#", "!", "$", "!", "#", "-", ".", " "]
    seed = random.randint(0, 100)
    land = ""

    print(f"We want to generate a landscape which is {cols} by {rows}")
    for row in range(rows):
        for col in range(cols):
            # Adding noise part 17
            n = pnoise2(row / rows, col / cols, base=seed)
            n *= 10
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += "\n"

    print("Finished gererating landscape")
    return land

def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(colored(question + "\n", "green"))

        if answer == "quit":
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Ooops this didnt make sense", "yellow"))
            tries += 1

    print(colored("Huh, this isn't fun anymore...", "red"))     
    quit()

cols = ask_for_number("How many columns? ")
rows = ask_for_number("How many rows? ")


output = generate_land(rows, cols)

print(output)
