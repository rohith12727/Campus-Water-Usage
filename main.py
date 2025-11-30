from classes import WaterUsage
import functions

#program for user interaction
def main():
    user_shower_data = input("About how many minutes do you spend showering per day?")
    user_flush_data = input("About how many times do you flush a toilet per day?")
    user_sink_data = input("About how many minutes do leave the sink on for per day?")
    user_dorm_data = input("what dorm do you reside in, PCV, Red Bricks, North Mountain, Yakitutu, Cerro Vista, or Sierra Madre")

    user_data = WaterUsage(int(user_shower_data), int(user_flush_data), int(user_sink_data), user_dorm_data.upper())

    print("Your daily water usage:", functions.user_average_water_usage(user_data))
    print(functions.user_suggestions(user_data))

    if functions.user_greatest_water_usage(user_data, user_dorm_data.upper()):
        print("You use MORE water than the average resident in", user_dorm_data)
    else:
        print("You use LESS water than the average resident in", user_dorm_data)

if __name__ == "__main__":
    main()
