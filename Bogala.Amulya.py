print("===== BMI Calculator =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

# BMI Formula
bmi = weight / (height ** 2)

print("\n===== Result =====")
print("Name:", name)
print("Age:", age)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("Your BMI is:", round(bmi, 2))

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nThank you for using the BMI Calculator!")