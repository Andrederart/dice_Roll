import random

user_dice_roll = random.randint(1, 6)
user_second_dice_roll = random.randint(1, 6)

computer_dice_roll = random.randint(1, 6)
computer_second_dice_roll = random.randint(1, 6)


if user_dice_roll + user_second_dice_roll > computer_dice_roll + computer_second_dice_roll:
            print("You win! You rolled the number " +
                str(user_dice_roll + user_second_dice_roll) +
                " While I rolled " +
                str(computer_dice_roll + computer_second_dice_roll))
else:
    print("You lose!!! I rolled the number " +
          str(computer_dice_roll + computer_second_dice_roll) +
          " against your " +
          str(user_dice_roll + user_second_dice_roll))