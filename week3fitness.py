import math

from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Enter your gender(m/f): ')
    birth_str = str(input('Enter DOB(ex: YYYY-MM-DD): '))
    weight = float(input('Enter your weight(in pounds): '))
    height = float(input('Enter your height(in inches): '))

    # Call the compute_age function to
    # compute the user's age in years.
    years = compute_age(birth_str)

    # Call the kg_from_lb function to
    # convert from pounds to kilograms.
    kgs = lbs_to_kgs(weight)

    # Call the cm_from_in function to
    # convert from inches to centimeters.
    cm = inch_to_cm(height)

    # Call the body_mass_index function.
    bmi = body_mass_index(weight, height)

    # Call the basal_metabolic_rate function.
    bmr = basal_metabolic_rate(gender, kgs, cm, years)

    # Print the results for the user to see.
    print(f"Age (years): {years}")
    print(f"Weight (kg): {kgs:.2f}")
    print(f"Height (cm): {cm:.2f}")
    print(f"Body mass index: {bmi:.2f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.2f}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")

    # Compute the difference between today and the
    # person's birthdate in years.
    today = datetime.now()
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def lbs_to_kgs(weight):
    kgs = abs(weight * 0.45359)
    return kgs

def inch_to_cm(height):
    cm = abs(height * 2.54)
    return cm

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = abs((10000 * weight) / (height**2))
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


main()