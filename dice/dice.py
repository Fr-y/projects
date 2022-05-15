from random import randint

# dice art
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}



# takes in the roll amounts
def roll_amount_input():
    dice = int(input("How many dice do you want to roll? [1-6] "))
    return dice if 0 < dice <= 6 else 0

# print out function
def generate_dices_vertical():
    # for the roll amounts
    roll_amount = roll_amount_input()
    if roll_amount > 0:
        for _ in range(roll_amount):
            # roll a random number
            rolled = (randint(1,6))
            # print out the dice by line
            for i in range(5):
                print(DICE_ART[rolled][i])
    elif roll_amount == 0:
        print("Please give an amount between 1 and 6")
        

def generate_dices_horizontal():
    roll_amount = roll_amount_input()
    if roll_amount > 0:
        rolls = [randint(1,6) for _ in range(roll_amount)]
        for i in range(5):
            dice_row = ''.join(DICE_ART[roll][i] for roll in rolls)
            print(dice_row)
    elif roll_amount == 0:
        print("Please give an amount between 1 and 6")


def main():
    choice = int(input("Generate vertically : [0] \nGenerate horizontally : [1]\n"))
    if choice == 0:
        generate_dices_vertical()
    elif choice == 1:
        generate_dices_horizontal()
    else:
        print("Please choose one: [0,1]")


# ------------main------------
main()
# ----------------------------