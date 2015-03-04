__author__ = 'Chris'

print("Welcome to the formula calculator.")
print("KEY:")
print("MPG ------ Calculate miles per gallon.")
print("KINETIC -- Calculate an object's kinetic energy.")
print("PAY -------Calculate pay for hours worked.")
print("FTM -------Convert feet to meters.")
print("YIELD -----Calculate labor yield.")
print("PERCENT ---Calculate labor percent.")
print("PROFIT ----Calculate profits given sales, cost of labor, and cost of sales.")
print("QUIT ------Close the calculator.")


# Calculate MPG taking in miles driven and gallons of fuel used
def mileage(miles_driven, gallons_used):
    mpg = float(miles_driven / gallons_used)
    return mpg


# Calculate kinetic energy (mass in kilograms, velocity in meters per second)
def kineteic_energy(mass, velocity):
    e = 0.5 * mass * velocity * velocity
    return e


# Calculate pay
def pay(hours, wage):
    if hours > 40:
        money = ((hours - 40) * wage * 1.5) + (40 * wage)
        return money
    else:
        money = hours * wage
        return money


# Convert feet to meters
def feet_to_meters(feet):
    meters = feet / 3.2808
    return meters


# Calculate labor yield (amount of money made per hour of labor used)
def labor_yield(sales, hours_used):
    lyield = float(sales / hours_used)
    return lyield


# Calculate labor percentage (percentage of sales that went to labor cost)
def labor_percent(sales, pay_used):
    percent = float((pay_used / sales) * 100)
    return percent


# Calculate profits
def profit(sales, pay_used, cost_sales):
    gain = float(sales - pay_used - cost_sales)
    return gain


# Allow user to choose which calculation they would like to perform
def choose():
        print(" ")
        print(" ")
        choice = input("What would you like me to calculate? Or type 'quit' to quit." + "\n>>>")
        if choice.upper() == "MPG":
            try:
                traveled = float(input("How many miles were traveled?"))
                fuel = float(input("How many gallons of fuel were used?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            miles_per_gallon = mileage(traveled, fuel)
            print("After traveling " + str(traveled) + " miles and using " + str(fuel) + " gallons of fuel. Your MPG was " + str(miles_per_gallon))
            choose()

        elif choice.upper() == "KINETIC":
            try:
                weight = float(input("How much does the object weight (in kilograms)?"))
                speed = float(input("What is the speed of the object (in meters per second)?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            energy = kineteic_energy(weight, speed)
            print("The kinetic energy of an object weighing " + str(weight) + " kilograms and moving " + str(speed) + " meters per second is " + str(energy) + " joules.")
            choose()

        elif choice.upper() == "PAY":
            try:
                hours_worked = float(input("How many hours were worked?"))
                pay_rate = float(input("What is the pay rate per hour?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            pay_check = pay(hours_worked, pay_rate)
            print("Working for " + str(hours_worked) + " hours at " + str(pay_rate) + " per hour. Your pay is " + str(pay_check) + " dollars.")
            choose()

        elif choice.upper() == "FTM":
            try:
                foot = float(input("How many feet would would you like to convert?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            meter = feet_to_meters(foot)
            print(str(foot) + " feet is " + str(meter) + " meters.")
            choose()

        elif choice.upper() == "YIELD":
            try:
                sales = float(input("How much is money was brought in(sales)?"))
                hours = float(input("How many labor hours were used?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            labor_y = labor_yield(sales, hours)
            print("For " + str(sales) + " in sales and " + str(hours) + " hours of labor used, labor yield is " + str(labor_y) + " dollars.")
            choose()

        elif choice.upper() == "PERCENT":
            try:
                sales = float(input("How much money was brought in(sales)?"))
                payroll = float(input("How much money was spent on labor?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            print("For " + str(sales) + " dollars in sales and " + str(payroll) + " dollars spent on labor, labor is " + str(labor_percent(sales, payroll)) + " percent.")
            choose()

        elif choice.upper() == "PROFIT":
            try:
                sales = float(input("How much money was brought in(sales)?"))
                payroll = float(input("How much money was spent on labor?"))
                cost_of_sales = float(input("How much did the merchandise cost?"))
            except ValueError:
                print("OOPS! That wasn't a number!")
                choose()
            profits = profit(sales, payroll, cost_of_sales)
            print("For " + str(sales) + " dollars in sales, " + str(payroll) + " dollars spent on labor and " + str(cost_of_sales) + " dollars spent on merchandise, profits are " + str(profits) + " dollars.")
            choose()

        elif choice.upper() == "QUIT":
            quit()

        else:
            print("I don't know that calculation, please try again.")
            choose()

choose()



