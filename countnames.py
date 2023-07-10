# program should count a specific name or - if none given - the occurences of all names.

#bonus: safe result in a file

import os

FILEPATH = "data/names"

#try to get list of whats in the folder

temp_filnamelist = os.listdir("data/names")

#making sure to just list real files

filenamelist = [name for name in temp_filnamelist if not os.path.isdir(os.path.join(FILEPATH, name))]


print(filenamelist)

# loop over name list , open it

for filename in filenamelist:
    with open(os.path.join(FILEPATH, filename), "r", encoding="UTF-8") as file:
        counter = 0
        for line in file:
            counter += 1
        print(filename + ": " + str(counter) + " entries")