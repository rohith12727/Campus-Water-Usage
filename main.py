from classes import WaterUsage
import functions
import data
from functions import Housing_average_dictionary

#Purpose: Asks the user for inputs on their water usage, including shower minutes, toilet flushes, sink minutes, and dorm name.
#Then turns these inputs into a WaterUsage data, and runs functions to show average water usage across dorms, compare the users water usage against the average of their dorm, and give recommendations on decreasing water usage.
#Input Type: Nothing
#Output Type: Nothing, text appears in console
#Example input: 9, 3, 10, PCV
#Example Output:
#Your average daily water usage: 49.3 Gallons
#The average daily water usage of PCV is 144.95 Gallons
#The average daily water usage of RED BRICKS is 66.6 Gallons
#The average daily water usage of NORTH MOUNTAIN is 79.19999999999999 Gallons
#The average daily water usage of YAKITUTU is 72.65 Gallons
#The average daily water usage of CERRO VISTA is 150.5 Gallons
#The average daily water usage of SIERRA MADRE is 88.65 Gallons
#You use LESS water than the average resident in PCV
#Good Work maintaining low water consumption, keep up what you are doing to help water conservation efforts!
#Structure: Store user inputs (received through input function/questions) in variables, then store data in WaterUsage object
#Run the user_data through the user_average_water_usage function and return user average water usage in gallons in a day.
#Print each dorms water usage average after running it through the build_housing_averages function and cycling through each dorm.
#Use user_greatest_water_usage function to compare user water usage against their dorm, and return string showing their water usage is either greater or lower (if statement) than their dorm average.
#Print recommendations based off of user_suggestions function.
def main():
    functions.build_housing_averages(data.data)

    user_shower_data = input("About how many minutes do you spend showering per day?")
    user_flush_data = input("About how many times do you flush a toilet per day?")
    user_sink_data = input("About how many minutes do leave the sink on for per day?")
    user_dorm_data = input("what dorm do you reside in, PCV, Red Bricks, North Mountain, Yakitutu, Cerro Vista, or Sierra Madre")

    user_data = WaterUsage(int(user_shower_data), int(user_flush_data), int(user_sink_data), user_dorm_data.upper())

    print("Your average daily water usage:", functions.user_average_water_usage(user_data), "Gallons")
    for dorm in Housing_average_dictionary:
        name = Housing_average_dictionary[dorm]
        print("The average daily water usage of", dorm,"is", name, "Gallons")

    if functions.user_greatest_water_usage(user_data, user_dorm_data.upper()):
        print("You use MORE water than the average resident in", user_dorm_data)
    else:
        print("You use LESS water than the average resident in", user_dorm_data)

    print(functions.user_suggestions(user_data))

if __name__ == "__main__":
    main()
