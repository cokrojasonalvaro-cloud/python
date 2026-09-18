print("BMI calculator")
weight = float(input("Massukan berat badan:"))
height = float(input("Massukan tinggi badan (dalam meter):"))
bmi = weight/(height*height)
print("BMI =", bmi)
if bmi<18.5:
    print("You are underweight")
elif 18.5<bmi<=25:
    print("You have a healthy weight")
elif 25<bmi<=30:
    print("You are overweight")
else:
    print("You are obese")