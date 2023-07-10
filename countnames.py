# program should count a specific name or - if none given - the occurences of all names.

#bonus: safe result in a file

import os

#try to get list of whats in the folder

temp_filnamelist = os.listdir("data/names")

#making sure to just list real files

filenamelist = [name for name in temp_filnamelist if not os.path.isdir(os.path.join("data/names", name))]


print(filenamelist)