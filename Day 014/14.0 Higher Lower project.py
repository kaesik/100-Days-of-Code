from HigherLower_arts import *
from HigherLower_functions import *

print(logo)
print("placeholder: welcome, play")
while True:
    score = 0
    person_a = fun_random_person()
    person_b = fun_random_person()
    while True:
        while person_a == person_b:
            person_b = fun_random_person()
        print("──────────────────────────────────────────")
        print(option_A)
        print(f"{fun_person_data(person_a)[0]}, {fun_person_data(person_a)[2]} from {fun_person_data(person_a)[3]}.")
        print(vs)
        print(option_B)
        print(f"{fun_person_data(person_b)[0]}, {fun_person_data(person_b)[2]} from {fun_person_data(person_b)[3]}.")
        print("──────────────────────────────────────────")
        guess = input("placeholder: write 'A' or 'B': ").lower()
        if guess == "a" and fun_win_round(fun_person_data(person_a)[1], fun_person_data(person_b)[1])\
                or guess == "b" and fun_win_round(fun_person_data(person_b)[1], fun_person_data(person_a)[1]):
            score += 1
            print(f"placeholder: gz, your score: {score}")
            if guess == "a":
                person_b = person_a
            elif guess == "b":
                person_a = person_b
        elif guess == "a" and fun_win_round(fun_person_data(person_b)[1], fun_person_data(person_a)[1])\
                or guess == "b" and fun_win_round(fun_person_data(person_a)[1], fun_person_data(person_b)[1]):
            print(f"placeholder: you lose, your score: {score}")
            break
        else:
            print("Incorrect decision. Please repeat.\n")
            continue
    game = input("placeholder: would you like play again? y/n\n").lower()
    if game != 'y':
        break
