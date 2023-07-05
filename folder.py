import os

print(os.listdir("."))
# lists the files in the location the program has been started in

globvar_filename = "testfile.txt"
globvar_path = 'C:/Users/stefa/Documents/Code/PycharmProjects/pythonProject2/'

def line_printer(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)

if globvar_filename in os.listdir("."):
    print("RELATIVE")
    line_printer(globvar_filename)

elif globvar_filename in os.listdir(globvar_path):
    print("ABSOLUTE")
    line_printer(globvar_path+globvar_filename)

else:
    print("file not found!")

