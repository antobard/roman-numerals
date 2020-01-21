# -*-coding:utf-8 -*
from roman_numerals import roman_converter, roman_num, roman_num_special
from random import randint, choice

def roman_numerals_rules():
    description_choice = ""
    while description_choice != 3:
        description_choice = int(input("What description do you want ? \n1. Roman Numerals\n2. Substractive Notation\n3. None\n"))
        if description_choice == 1:
            print("Here are all Roman Numerals and their values :")
            for i in roman_num:
                print("{} = {}".format(i[0], i[1]))
        elif description_choice == 2:
            print("If a value placed before another is inferior to it, it must be substracted to it")
            random_sub = choice(roman_num_special)
            print("For exemple : {} = {}".format(random_sub[0], random_sub[1]))


def roman_num_quiz():
    roman_numerals_rules()
    continue_game = True
    while continue_game:
        random_number = randint(1, 4000)
        guess_type = choice(["roman", "decimal"])
        if guess_type == "decimal":
            random_number = roman_converter(random_number)
        guess = ""
        while guess != str(roman_converter(random_number)):
            guess = input("Try to convert {} into {} notation : ".format(random_number, guess_type))
        print("Well Done !")
        quit_choice = input("One more time ? \n1. Yes\n2. No\n")
        if quit_choice == "2":
            continue_game = False
    

if __name__ == "__main__":
    import os
    roman_num_quiz()
    os.system('pause')