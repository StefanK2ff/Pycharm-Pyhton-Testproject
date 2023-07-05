import os

#print(os.listdir("."))
# lists the files in the location the program has been started in

globvar_filename = "testfile.txt"
globvar_path_replaced = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace("\\","/")
globvar_filepath_replaced = os.path.abspath(os.path.join(os.path.dirname(__file__),globvar_filename)).replace("\\","/")

# os.path.join will use a as specific slash

# os.listdir will bring all files and folder in a dir

# os.path.isdir checks if element in dir is file or directory

def line_printer(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)

if globvar_filename in os.listdir("."):
    print("RELATIVE")
    line_printer(globvar_filename)

elif globvar_filename in os.listdir(globvar_path_replaced):
    print("ABSOLUTE")
    line_printer(globvar_filepath_replaced)

else:
    print("file not found!")

