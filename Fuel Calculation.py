a=int(input("Enter the no of liters to fill the tank "))
b=int(input("Enter the distance covered "))
c=(b*0.6214)/(a*0.2642)
if a<=0:
    print(a,"  is an Invalid Input")
else:
    print("Liters/100KM",round((a/b)*100,2))
    print("Miles/gallons",round(c,2))
