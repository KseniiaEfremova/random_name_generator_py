import random


def get_random_names() -> list:
    """
    The function asks the user for a list of names and number and returns random names from this a list
    """
    users_list_of_names = input("Input list of names: ").split()

    # checking a number of entered names
    while len(users_list_of_names) < 2:
        users_list_of_names = input("Input more than one name, please: ").split()
    number_of_random_names = int(input("Input the number of names, that you want to get: "))

    # check a wrong entered number
    while number_of_random_names >= len(users_list_of_names):
        print("Wrong number! Try again.")
        number_of_random_names = int(input("Input the number of names, that you want to get: "))

    return random.choices(users_list_of_names, k=number_of_random_names)


print(get_random_names())
