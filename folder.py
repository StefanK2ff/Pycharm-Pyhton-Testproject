import os

print(os.listdir("."))
# lists the files in the location the program has been started in

if "testfile.txt" in os.listdir("."):
    with open("testfile.txt", "r") as file:
        for line in file:
            print(line)
else:
    print("file not found!")

    