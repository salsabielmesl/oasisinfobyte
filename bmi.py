weight = float(input("Enter you'r weight in kilos: "))
height = float(input("Enter you'r hight in meters: "))
BMI = weight/(height * height)
print(BMI)

if BMI < 18.5:
    print("underweight")
elif BMI >18.5 and BMI <24.9:
    print("normal weight")
elif BMI >25 and BMI <29.9:
    print("overweight")
elif BMI >30 and BMI <34.9:
    print("obese")
elif BMI >35.5 and BMI <39.9:
    print("severely obese")
else:
    print("morbidly obese")