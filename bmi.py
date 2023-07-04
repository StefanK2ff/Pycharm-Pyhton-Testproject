# pseudocode for BMI calculator
# welcome message, display what's going to happen
# ask for height in cm
# ask for weight in kgs
# calc BMI, weight / height ** 2

# ideas:
# check if numbers make sense (add lower and upper thresholds

globvar_welcome_message = "Welcome, this is an two-step BMI calculator. After you typed your height, it will aks your weight."

def calc_bmi (weight, height):
    return weight / height ** 2


print(globvar_welcome_message)

height = int(input("Please provide your height in cm: "))
weight = int(input("Please provide your weight in kgs: "))

print(f"Your BMI is {calc_bmi(height, weight)}")
