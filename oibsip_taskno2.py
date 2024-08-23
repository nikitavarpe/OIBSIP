def BMI(height, weight):
    bmi= float(weight/(height**2))
    return bmi

def Calculator(bmi):
    if bmi<18.5:
        print ("Underweight")

    elif (18.5<bmi<24.9):
        print ("Normal Weight")

    elif (25<bmi<29.9):
        print ("Overweight")

    else:
        print ("Obese")

height= float(input("Enter height in meters:"))
weight= float(input("Enter weight in kgs:"))

bmi=BMI(height, weight)
print (f"Your BMI is: {bmi:.2f}")
Calculator(bmi)