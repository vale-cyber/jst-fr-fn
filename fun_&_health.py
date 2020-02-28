import math
import random


def main():
    main_menu()
    choice = int(input(">> "))

    if choice == 1:
        print()
        print("\t" + chuck_norris_jokes())

    elif choice == 2:
        print()
        print(quotes())

    elif choice == 3:
        print()
    elif choice == 4:
        display_menu_health()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Unique Banner
            tittle = "Lets calculate your BMI"
            tittle_with_spaces = " ".join(tittle)
            banner = "<><><><><><><><><><>" + " | " + tittle_with_spaces + " | " + "<><><><><><><><><><>" + "\n"
            print(banner)

            # User Input
            weight = float(input("Weight in pounds: "))
            height = float(input("Height in inches: "))
            print()

            print("BMI Results")

            # Call BMI compute function
            BMI = compute_bmi(weight, height)

            # Display BMI in correct format
            print('BMI is ' + '{0:.2f}'.format(BMI))

            # Call BMI assess Function

            print('BMI Classification: ', assess_bmi(BMI))

        if choice == 2:
            # Unique Banner
            tittle = "YMCA"
            tittle_with_spaces = " ".join(tittle)
            banner = '~.~.~.~.~.~.~.~.~.~.~' + " | " + tittle_with_spaces + " | " + '~.~.~.~.~.~.~.~.~.~.~' + "\n"
            print(banner)

            # Get user input
            weight = float(input('What is your weight in pounds? '))
            waist = float(input("What is your waist size in inches? "))
            gender = input("What is your gender (M/F)? ")
            print()

            print("YMCA Results ")

            fat_percent = ymca(weight, waist, gender)
            print("YMCA Classification: ", body_fat_classification(gender, fat_percent))

        if choice == 3:
            # Unique Banner
            tittle = "NAVY"
            tittle_with_spaces = " ".join(tittle)
            banner = "<><><><><><><><><><>" + " | " + tittle_with_spaces + " | " + "<><><><><><><><><><>" + "\n"
            print(banner)

            # Get user input
            weight = float(input("what is your weight in pounds? "))
            height = float(input("What is your height in inches? "))
            abdomen = float(input('What is your abdomen measurements in inches? '))
            neck = float(input("What is your neck measurement in inches? "))
            gender = input("What is your gender (M/F)? ")
            if gender == "F":
                hip = float(input("What is your hip measurements? "))
                print()
                print("Here is your NAVY analysis: ")
                fat_percent = navy_female(weight, height, abdomen, neck, hip)
            else:
                print()
                print("Here is your NAVY analysis: ")
                fat_percent = navy_male(weight, height, abdomen, neck)

            print("NAVY Classification: ", body_fat_classification(gender, fat_percent))

        if choice == 4:
            # Unique Banner
            tittle = "ALL"
            tittle_with_spaces = " ".join(tittle)
            banner = "((_(__(___(____(_____(______(       " + tittle_with_spaces + "       )______)_____)____)___)__)_))"
            print(banner)

            weight = float(input("what is your weight in pounds? "))
            height = float(input("What is your height in inches? "))
            waist = float(input("What is your waist size in inches? "))
            abdomen = float(input('What is your abdomen measurements in inches? '))
            neck = float(input("What is your neck measurement in inches? "))
            gender = input("What is your gender (M/F)? ")
            if gender == "F":
                hip = float(input("What is your hip measurements? "))
                print()
                print("Here is your analysis: ")
                print()
            else:
                print("Here is your analysis: ")
                print()

            print("BMI Results:")
            # Call BMI compute function
            BMI = compute_bmi(weight, height)
            # Display BMI in correct format
            print('BMI is ' + '{0:.2f}'.format(BMI))
            # Call BMI assess Function

            print('BMI Classification: ', assess_bmi(BMI))
            print()

            print("YMCA Results:")
            # YMCA analysis
            fat_percent = ymca(weight, waist, gender)

            print("YMCA Classification: ", body_fat_classification(gender, fat_percent))
            print()

            print("NAVY Results:")
            # NAVY analysis
            if gender == "F":
                fat_percent = navy_female(weight, height, abdomen, neck, hip)
            elif gender == "M":
                fat_percent = navy_male(weight, height, abdomen, neck)
            print("NAVY Classification: ", body_fat_classification(gender, fat_percent))


def main_menu():
    title = " le MAIN menu "
    title_with_spaces = " ".join(title)
    print('.-.-.-.-.- ' + title_with_spaces + ' -.-.-.-.-.')
    print('.--.--.--.--.--. Pick one .--.--.--.--.--.--.--.')
    print('')
    print("1) Chuck Norris")
    print("2) Quotes")
    print("3) tic-tac-toe")
    print("4) Health")


# ______________________________________________Choice 1) Chuck Norris_____________________________________________

def chuck_norris_jokes():
    for x in range(20):
        joke_number = random.randint(1, 21)
        if joke_number == 1:
            joke = "Chuck Norris threw a grenade and killed 50 people, then it exploded."
        elif joke_number == 2:
            joke = "Chuck Norris invented the Olympic Games in hopes of finding a worthy opponent."
        elif joke_number == 3:
            joke = "Death once had a near-Chuck-Norris experience."
        elif joke_number == 4:
            joke = "Once a cobra bit Chuck Norris' leg. After five days of excruciating pain, the cobra died."
        elif joke_number == 5:
            joke = "Chuck Norris can kill two stones with one bird."
        elif joke_number == 6:
            joke = "Chuck can set ants on fire with a magnifying glass. At night."
        elif joke_number == 7:
            joke = "Chuck Norris can hear sign language."
        elif joke_number == 8:
            joke = "Chuck Norris makes onions cry."
        elif joke_number == 9:
            joke = "Chuck Norris knows Victoria's secret."
        elif joke_number == 10:
            joke = "Chuck Norris counted to infinity. Twice."
        elif joke_number == 11:
            joke = "Chuck Norris beat the sun in a staring contest."
        elif joke_number == 12:
            joke = "Chuck Norris can build a snowman out of rain."
        elif joke_number == 13:
            joke = "Giraffes were created when Chuck Norris uppercutted a horse."
        elif joke_number == 14:
            joke = "If it looks like chicken, tastes like chicken, and feels like chicken but Chuck Norris says its " \
                   "beef, then it's beef. "
        elif joke_number == 15:
            joke = "Chuck Norris can speak braille."
        elif joke_number == 16:
            joke = "Chuck Norris can pick oranges from an apple tree and make the best lemonade you've ever tasted."
        elif joke_number == 17:
            joke = "Chuck Norris will never have a heart attack... even a heart isn't foolish enough to attack Chuck " \
                   "Norris. "
        elif joke_number == 18:
            joke = "Chuck Norris doesnt wear a watch. He decides what time it is."
        elif joke_number == 19:
            joke = "Chuck Norris beat Halo 1, 2, and 3 on Legendary with a broken Guitar Hero controller."
        elif joke_number == 20:
            joke = "Chuck Norris doesn't dial the wrong number, you pick up the wrong phone."
        return joke


# ______________________________________________Choice 2) Quotes_____________________________________________

def quotes():
    for x in range(20):
        quote_number = random.randint(1, 21)
        if quote_number == 1:
            quote = "You don't get what you deserve, you get what you take."
        elif quote_number == 2:
            quote = "If opportunity doesn't knock, build a door."
        elif quote_number == 3:
            quote = "Power belongs to the people who take it."
        elif quote_number == 4:
            quote = "If I don't listen to my imaginary friend why should I listen to yours?"
        elif quote_number == 5:
            quote = "I don't want to be a product of my environment. I want my environment to be a product of me."
        elif quote_number == 6:
            quote = "life is a long journey with a map writen by a fool."
        elif quote_number == 7:
            quote = "The greatest glory in living lies not in never falling, but in rising every time we fall."
        elif quote_number == 8:
            quote = "Life is what happens when you're busy making other plans."
        elif quote_number == 9:
            quote = "When you reach the end of your rope, tie a knot in it and hang on."
        elif quote_number == 10:
            quote = "Always remember that you are absolutely unique. Just like everyone else."
        elif quote_number == 11:
            quote = "Don't judge each day by the harvest you reap but by the seeds that you plant."
        elif quote_number == 12:
            quote = "It is during our darkest moments that we must focus to see the light."
        elif quote_number == 13:
            quote = "Do not go where the path may lead, go instead where there is no path and leave a trail."
        elif quote_number == 14:
            quote = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction " \
                    "you choose. "
        elif quote_number == 15:
            quote = "Love the life you live. Live the life you love."
        elif quote_number == 16:
            quote = "The way to get started is to quit talking and begin doing."
        elif quote_number == 17:
            quote = "A successful man is one who can lay a firm foundation with the bricks others have thrown at him."
        elif quote_number == 18:
            quote = "Try not to become a man of success. Rather become a man of value."
        elif quote_number == 19:
            quote = "The only place where success comes before work is in the dictionary."
        elif quote_number == 20:
            quote = "If you are not willing to risk the usual, you will have to settle for the ordinary."
        return quote


# _______________________________________________Choice 4) Health_____________________________________________
def display_menu_health():
    # le HEALTH menu
    title = " le menu "
    title_with_spaces = " ".join(title)
    print('.-.-.-.-.- ' + title_with_spaces + ' -.-.-.-.-.')
    print('1) BMI Calculator')
    print('2) YMCA')
    print('3) NAVY')
    print('4) All')


def compute_bmi(weight, height):
    BMI_FACTOR = 703

    # Calculate the BMI
    BMI = (BMI_FACTOR * weight) / height ** 2
    return BMI


def assess_bmi(BMI):
    # using if and elif statements give conditions for BMI classifications
    if BMI <= 18.5:
        classification = 'Under Weight'
    elif 18.5 < BMI <= 24.99:
        classification = 'Normal Weight'
    elif 25 < BMI <= 29.99:
        classification = 'Over Weight'
    elif 30 < BMI <= 34.99:
        classification = 'Obesity (class1)'
    elif 35 < BMI <= 39.99:
        classification = 'Obesity (class2)'
    else:
        classification = 'Morbid Obesity'

    return classification


def ymca(weight, waist, gender):
    # Constants
    CONSTANT_WOMEN_1 = -76.76
    CONSTANT_MEN_1 = -98.42
    COMMON_CONSTANT_1 = 4.15
    COMMON_CONSTANT_2 = .082

    # determine which equation to use

    # Female YMCA analysis
    if gender == "F":
        fat_percent = ((CONSTANT_WOMEN_1 + (COMMON_CONSTANT_1 * waist)) - (COMMON_CONSTANT_2 * weight)) / weight
        print('Your YMCA body fat % is: ' + '{:.2f}%'.format(fat_percent * 100))

        # Fat Mass
        fat_mass = fat_percent * weight
        print('YMCA Fat Mass: ' + '{0:.2f}'.format(fat_mass))

        # Lean Mass
        lean_mass = weight - fat_mass
        print("YMCA Lean Mass: " + '{0:.2f}'.format(lean_mass))

        return fat_percent

    # Male YMCA analysis
    elif gender == "M":
        fat_percent = ((CONSTANT_MEN_1 + (COMMON_CONSTANT_1 * waist)) - (COMMON_CONSTANT_2 * weight)) / weight
        print('Your YMCA body fat % is: ' + '{0:.2f}%'.format(fat_percent * 100))

        # Fat Mass
        fat_mass = fat_percent * weight
        print('YMCA Fat Mass: ' + '{0:.2f}'.format(fat_mass))

        # Lean Mass
        lean_mass = weight - fat_mass
        print("YMCA Lean Mass: " + '{0:.2f}'.format(lean_mass))

        return fat_percent


def navy_female(weight, height, abdomen, neck, hip):
    # Constants
    CONSTANT_WOMEN_1 = 163.205
    CONSTANT_WOMEN_2 = 97.684
    CONSTANT_WOMEN_3 = 78.387
    COMMON_CONSTANT = .01

    # Female NAVY analysis
    fat_percent = ((CONSTANT_WOMEN_1 * (math.log10(abdomen + hip - neck))) - (
            CONSTANT_WOMEN_2 * (math.log10(height))) - CONSTANT_WOMEN_3) * COMMON_CONSTANT
    print('Your NAVY body fat % is: ' + '{:.2f}%'.format(fat_percent * 100))

    # Fat Mass
    fat_mass = fat_percent * weight
    print('NAVY Fat Mass: ' + '{:.2f}'.format(fat_mass))

    # Lean Mass
    lean_mass = weight - fat_mass
    print("NAVY Lean Mass: " + '{:.2f}'.format(lean_mass))

    return fat_percent


def navy_male(weight, height, abdomen, neck):
    # Constants
    CONSTANT_MEN_1 = 86.010
    CONSTANT_MEN_2 = 70.041
    CONSTANT_MEN_3 = 36.76
    COMMON_CONSTANT = .01

    # Male NAVY analysis
    fat_percent = ((CONSTANT_MEN_1 * (math.log10(abdomen - neck))) - (
            CONSTANT_MEN_2 * (math.log10(height))) + CONSTANT_MEN_3) * COMMON_CONSTANT

    print('Your NAVY body fat % is: ' + '{:.2f}%'.format(fat_percent * 100))

    # Fat Mass
    fat_mass = fat_percent * weight
    print('NAVY Fat Mass: ' + '{:.2f}'.format(fat_mass))

    # Lean Mass
    lean_mass = weight - fat_mass
    print("NAVY Lean Mass: " + '{:.2f}'.format(lean_mass))

    return fat_percent


def body_fat_classification(gender, fat_percent):
    # Female categories
    if gender == "F":
        if .10 <= fat_percent <= .13:
            classification = "Essential Fat"
        elif .14 <= fat_percent <= .20:
            classification = 'Athlete'
        elif .21 <= fat_percent <= .24:
            classification = "Fitness"
        elif .25 <= fat_percent <= .31:
            classification = "Acceptable"
        else:
            classification = "obese"

        return classification

    # Male categories
    if gender == "M":
        if .02 <= fat_percent <= .05:
            classification = "Essential Fat"
        elif .06 <= fat_percent <= .13:
            classification = 'Athlete'
        elif .14 <= fat_percent <= .17:
            classification = "Fitness"
        elif .18 <= fat_percent <= .24:
            classification = "Acceptable"
        else:
            classification = "obese"
        return classification


main()
