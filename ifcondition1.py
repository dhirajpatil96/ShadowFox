height = float(input("enter the height in metres:"))
weight = float(input("enter weight in kilograms:"))
bmi = weight/height**2
print(bmi)
if bmi>=30:
    print("obesity")
elif bmi>=25:
    print("overweight")
elif bmi>=18.5:
    print("normal")
elif bmi<18.5:
    print("underweight")
    
    
