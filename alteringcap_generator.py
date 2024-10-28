import random

final_sentence = ""

not_over = True

def randomize_sentence():
    for letter in sentence:

        global final_sentence

        rng = random.randint(1,2)
        if rng == 1:
            final_sentence += letter.upper() 
        else:
            final_sentence += letter.lower()

def randomize_5times():
    global final_sentence
    for i in range(1, 6):
        randomize_sentence()
        print(final_sentence)
        final_sentence = ''

while not_over:
    
    sentence = input("Type the sentence you want the altering cap in: \n")

    print('\n')

    randomize_5times()
    
    print("Copy using ctrl + shift + c")

    print('\n')

    direction = input("Would you like to regenrate the same sentences, Y or N? ").lower()

    if direction == 'y':

        user_not_satisfied = True

        while user_not_satisfied:

            randomize_5times()

            direction = input("Would you like to regenrate the sentence, Y or N? ").lower()

            if direction == 'n':
                print("\n")
                break

    
    
    direction2 = input("Would you like to go again with a different sentence, y or n? ").lower()

    if direction2 == 'n':
        not_over = False
    else:
        sentence = ""

