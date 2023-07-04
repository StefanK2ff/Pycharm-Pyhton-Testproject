import os
import getpass


# functions
def print_hi(name, loc):
    print(f'Hi, {name} - I\'m, existing in {loc}')


def get_location():
    # I try to get the files position back
    return os.path.abspath(__file__)


def get_username():
    return getpass.getuser()


def get_custom_username():
    resp = input("Please provide a custom name: ")
    return resp


# program start

if __name__ == '__main__':
    print_hi(get_username(), get_location())

response = "x"
while response != ["Y", "y", "N", "n"]:
    response = input("Do you want to override the name of this message? (Y/N)")
    match response:
        case "Y" | "y":
            print("You selected 'yes'")
            print_hi(get_custom_username(), get_location())
            break
        case "N" | "n":
            print("Ok, doing nothing, shutting down")
            break
        case other:
            print("Invalid Input, please try again")
