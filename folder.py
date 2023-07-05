import os

#print(os.listdir("."))
# lists the files in the location the program has been started in

globvar_filename = "testfile.txt"
globvar_path_replaced = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace("\\","/")
globvar_path_replaced_file = os.path.abspath(os.path.join(os.path.dirname(__file__),globvar_filename)).replace("\\","/")

def line_printer(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)

if globvar_filename in os.listdir("."):
    print("RELATIVE")
    line_printer(globvar_filename)

elif globvar_filename in os.listdir(globvar_path_replaced):
    print("ABSOLUTE")
    line_printer(globvar_path_replaced_file)

else:
    print("file not found!")

