def calculate_bmi(height, weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    #Add code here to calculate BMI
    bmi=weight/(height*height)

    #Add code here to display calculate BMI
    print(round(bmi,1))

    #Part (d)
    if(bmi < 18.5):
        print("Under Weight")
        return -1
    
    elif(18.5 <= bmi <= 25.0):
        print("Normal Weight")
        return 0
    
    else:
        print("Over Weight")
        return 1

try:
    height = float(input("Enter height in meters (e.g., 1.73): "))
    weight = float(input("Enter weight in kilograms (e.g., 57): "))

    result = calculate_bmi(height, weight)
    print("Return Value:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")