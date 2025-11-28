from classes import WaterUsage
import functions

def main():
    user_shower_data = input("How many minutes do you spend showering per day?")
    user_flush_data = input("How many times do you spend flush per day?")
    user_sink_data = input("How many minutes do leave the sink on for per day?")
    user_dorm_data = input("what dorm do you reside in, PCV, Red Bricks, North Mountain, Yakitutu, Cerro Vista, or Sierra Madre")

    user_data = WaterUsage(int(user_shower_data), int(user_flush_data), int(user_sink_data), user_dorm_data)

    print(functions.user_average_water_usage(user_data))

    print(functions.user_suggestions(user_data))

if __name__ == "__main__":
    main()
