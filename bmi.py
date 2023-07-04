# pseudocode for BMI calculator
# welcome message, display what's going to happen
# ask for height in cm
# ask for weight in kgs
# calc BMI, weight / height ** 2

# ideas:
# check if numbers make sense (add lower and upper thresholds

globvar_welcome_message = "Welcome, this is a two-step BMI calculator. After you typed your height, it will aks your " \
                          "weight."


def calc_bmi(weight, height):
    return weight / height ** 2


def input_digit_validator(inp):
    if inp.isdigit():
        return int(inp)
    else:
        print("Wrong input, please retry!")
        return False


height = False  # Initialize the variable with a default value
weight = False

print(globvar_welcome_message)

while height is False:  # Loop until a valid input is provided
    height = input_digit_validator(input("Please provide your height in cm: "))

while weight is False:  # Loop until a valid input is provided
    weight = input_digit_validator(input("Please provide your weight in kgs: "))

print(f"Your BMI is {calc_bmi(height, weight)}")
