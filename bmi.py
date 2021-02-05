"""
This is a simple python application that calculates the Body Mass Index in metrics and imperrial standard
using formula:- BMI = M/H**2
where M= Mass in kilogram and H = Height in centimetre for metrics
where M= Mass in kilogram and H = Height in centimetre for metrics
 
BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
"""



# this calculates Body Mass Index using Metrics standard
def bmi_metrics():
    weight = float(input("enter your mass in kilogram (KG) : " ))
    height = float(input("enter your height in metres(M) : " ))
    bmi = weight * (height**2)
    print("your body mass index = ".capitalize(), bmi, " kg/m2")

    if bmi <= 18.5 :
        print("you are below standard body mass, you should eat food rich in fats and eat regularly".capitalize())
        bmi_calculator()

    elif bmi >= 18.5 and bmi <= 24.9:
        print("you have a normal standard weight".upper())
        bmi_calculator()

    elif bmi >= 25 and bmi <= 29.9:
        print("you over weighed normal standard weight".upper())
        bmi_calculator()

    else: 
        print("you have obesity and needs quick medical attention".upper())
        response = input("Do you wish to continue? type Y for (yes) or N for (no): ")
        if response == "y" or response == "Y":
            bmi_calculator()
        elif response == "n" or response == "N":
            print(" Thanks for using this program ")
            exit()


# This calculates Body Mass Index using Imperial standard
def bmi_imperial():
    """
    DOCTYPE:
    1kg = 2.2lbs :-> converting kilograms to pounds
    1inch = 0.0254m :-> Cconverting inches to meters
    To convert your body weight from kg to lbs, you multiply kilograms by 2.2
    To convert your height from meters to inches, take your height in meters and divide by 0.0254
    """
    weightInKilogram = float(input("enter your mass in kilogram (kg) : "))
    heightInMeters = float(input("enter your height in metres(m) : " ))
    weight = weightInKilogram * 2.2  # covert kg to pounds
    height = heightInMeters / 0.0254 # convert meters to inches
    bmi = (weight * 703)/(height**2)
    print("your weight in pounds = ", weight, "lbs")
    print("your height in inches = ", height, "inches")
    print("your body mass index = ".capitalize() , bmi, "lbs/inches2")

    if bmi <= 18.5 :
        print("you are below standard body mass, you should eat food rich in fats and eat regularly".capitalize())

    elif bmi >= 18.5 and bmi <= 24.9:
        print("you have a normal standard weight".capitalize())
        bmi_calculator()

    elif bmi >= 25 and bmi <= 29.9:
        print("you over weighed normal standard weight".capitalize())
        bmi_calculator()

    else: 
        print("you have obesity and needs quick medical attention".capitalize())
        response = input("Do you wish to continue? type Y for (yes) or N for (no): ")
        if response == "y" or response == "Y":
            bmi_calculator()
        elif response == "n" or response == "N":
            print(" Thanks for using this program ")
            exit()


# This is the main and it computes the BMI with either standard based on user response
def bmi_calculator():
    print("""
    ******************************************************************
            Welcome to Body Mass Index Calculator (BMI = M/H**2)
    ******************************************************************
    """)

    #Ask if user would like to use Metric or Imperial units
    response = input("would you like to calculate your Body Mass Index in Metrics or Imperial, type Metrics or Imperial: ").lower()
    
    if response == 'metrics':
        print("---------you have chosen to compute your BMI in---------", response.upper())
        bmi_metrics() # This calls and computes the metrics standard function

    elif response == 'imperial':
        print("---------you have chosen to compute your BMI in---------", response.upper())
        return bmi_imperial()# This calls and computes the imperial standard function

    else:
        print("invalid response please try again".capitalize())
        bmi_calculator()
bmi_calculator()
