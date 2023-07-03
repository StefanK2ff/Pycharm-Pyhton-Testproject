
import os
import getpass

def print_hi(name, loc):

    print(f'Hi, {name} - I\'m, existing in {loc}')

def get_location():
    # I try to get the files position back
    return os.path.abspath(__file__)

def get_username():
    return getpass.getuser()



if __name__ == '__main__':
    print_hi(get_username(), get_location())

response = input("Do you want to override the name of this message? (Y/N)")

match response:
    case "Y", "y":
        print("You chose Yes")
    case "N", "n":
        print("Yoi said no.")


