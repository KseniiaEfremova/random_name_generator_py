import random


def get_list_of_users_names() -> list:
    """
    The function asks the user to input a list of names, checks and returns it.
    """
    users_input = input("Input list of names separated by comma: ").split(",")
    users_list_of_names = [name.strip() for name in users_input]

    # checking a number of entered names
    while len(users_list_of_names) < 2:
        users_input = input("Input more than one name, please: ").split(",")
        users_list_of_names = [name.strip() for name in users_input]

    return users_list_of_names


def get_number_of_names(list_of_names: list) -> int:
    """
    The function asks the user to input a number of names, that he wants to get, checks and returns it.
    """

    try:
        user_number = int(input("Input the number of names, that you want to get: "))
    except ValueError:
        print("Your number should be an integer! Try again.")
        user_number = int(input("Input the number of names, that you want to get: "))

    while True:
        # check a wrong entered number
        if user_number >= len(list_of_names):
            print("Your number should be less than the number of names in the list! Try again.")
            user_number = int(input("Input the number of names, that you want to get: "))
        elif user_number == 0:
            print("Your number shouldn't be zero integer! Try again.")
            user_number = int(input("Input the number of names, that you want to get: "))
        elif user_number < 0:
            print("Your number shouldn't  be a negative integer! Try again.")
            user_number = int(input("Input the number of names, that you want to get: "))
        else:
            return user_number



# print(get_number_of_names(get_list_of_users_names()))

def get_random_names(list_of_names: list, number: int):
    """
    The function takes the list of names and number and returns random names from this list
    """

    print(random.choices(list_of_names, k=number))


user_names_list = get_list_of_users_names()
number = get_number_of_names(user_names_list)

get_random_names(user_names_list, number)
