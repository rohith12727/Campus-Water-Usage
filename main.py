from classes import WaterUsage
import functions
import data
from functions import Housing_average_dictionary

def main():
    functions.build_housing_averages(data.data)

    user_shower_data = input("About how many minutes do you spend showering per day?")
    user_flush_data = input("About how many times do you flush a toilet per day?")
    user_sink_data = input("About how many minutes do leave the sink on for per day?")
    valid_dorms = {"PCV", "RED BRICKS", "NORTH MOUNTAIN", "YAKITUTU", "CERRO VISTA", "SIERRA MADRE"}

    user_dorm_data = ""
    while user_dorm_data not in valid_dorms:
        user_dorm_data = input("What housing do you live in? (PCV, Red Bricks, North Mountain, Yakitutu, Cerro Vista, Sierra Madre): ").upper()
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
