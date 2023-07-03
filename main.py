# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import getpass

def print_hi(name, loc):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} - I\'m, existing in {loc}')  # Press Strg+F8 to toggle the breakpoint.

def get_location():
    # I try to get the files position back
    return os.path.abspath(__file__)

def get_usernamer():
    return getpass.getuser()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(get_usernamer(), get_location())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
