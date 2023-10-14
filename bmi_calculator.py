height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))
# calculating body mass index
bmi = weight / height ** 2

# declaring empty message
message = ''

# assigning message as per the bmi calculated
if bmi < 18.5:
    message = "You are underweight"
elif bmi >= 18.5 and bmi < 25:
    message = "You have normal weight"
elif bmi >= 25 and bmi < 30:
    message = "You are overweight"
elif bmi >= 30 and bmi < 35:
    message = "You are obese"
else:
    message = "You are clinically obese"

print("Your BMI is ", round(bmi, 2), ' and ', message)
