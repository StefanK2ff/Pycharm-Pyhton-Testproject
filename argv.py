import sys

print(sys)
print(sys.argv)


def linecounter(file):
    counter = 0
    for line in file:
        counter = counter + 1
    return counter


if len(sys.argv) >= 2:
    resp = ""
    while resp != "9":
        resp = input("Menu: Count Lines of file [1]. Exit [9]. Your choice: ")
        match resp:
            case "1":
                print(f"File contains {linecounter(open(sys.argv[1], 'r'))} lines")
            case "9":
                print("shutting down")
            case other:
                print("wrong input, try again")
else:
    print("Noting to do here. Forgot parameter?")
