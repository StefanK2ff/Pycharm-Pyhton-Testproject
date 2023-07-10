# program should count a specific name or - if none given - the occurences of all names.

#bonus: safe result in a file

import os

FILEPATH = "data/names"
SEARCHTERM = "Max"

counter = 0

for filename in os.listdir(FILEPATH):
    filepath = os.path.join(FILEPATH, filename)

    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="UTF-8") as file:
            for line in file:
                if line.split(" ")[0] == SEARCHTERM:
                    counter += 1

print(SEARCHTERM + " was found " + str(counter) + " times")