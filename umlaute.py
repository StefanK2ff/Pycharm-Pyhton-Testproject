import os

filename = os.path.join(os.path.dirname(__file__), "umlaute.txt")

with open(filename, "r") as file:
    for line in file:
        print(line)