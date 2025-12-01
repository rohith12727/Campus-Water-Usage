from classes import WaterUsage
import data

Housing_average_dictionary = {"PCV": 0, "RED BRICKS": 0, "NORTH MOUNTAIN": 0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE": 0}

#Purpose: Takes in float value representing minutes and converts it to gallons of water.
#Input Type: float
#Output Type: float
#Input Example: 6
#Output Example: 15
#Structure: Multiply minutes by 2.5 (gotten from EPA website average shower water usage per minute).
#Round by 3 decimal points, and return value.
def shower_water_conversion(minutes: float) -> float:
    gallons = round(minutes * 2.5, 3)
    return gallons

#Purpose: Takes in float value representing minutes and converts it to gallons of water.
#Input Type: float
#Output Type: float
#Input Example: 6
#Output Example: 13.2
#Structure: Multiply minutes by 2.2 (gotten from EPA website average shower water usage per minute).
#Round by 3 decimal points, and return value.
def sink_water_conversion(minutes: float) -> float:
    gallons = round(minutes * 2.2, 3)
    return gallons

#Purpose: Takes in float value representing minutes and converts it to gallons of water.
#Input Type: float
#Output Type: float
#Input Example: 6
#Output Example: 13.2
#Structure: Multiply minutes by 1.6 (gotten from EPA website average shower water usage per minute).
#Round by 3 decimal points, and return value.
def flushes_water_conversion(flushes: float) -> float:
    gallons = round(flushes * 1.6, 3)
    return gallons

#Purpose: Calculates average water usage based on dorm input name and list of WaterUsage data.
#Input Type: list[WaterUsage], str
#Output Type: float
#Input Example: [WaterUsage(45, 5, 10, "PCV"), WaterUsage(30, 4, 5, "RED BRICKS"), WaterUsage(20, 3, 10, "NORTH MOUNTAIN"), WaterUsage(15, 6, 15, "YAKITITU"), WaterUsage(20, 4, 15, "SIERRA MADRE"), WaterUsage(45, 5, 30, "CERRO VISTA"), WaterUsage(30, 4, 30, "PCV"), WaterUsage(10, 3, 5, "RED BRICKS"), WaterUsage(20, 6, 10, "NORTH MOUNTAIN"), WaterUsage(18, 3, 7, "YAKITITU"), WaterUsage(25, 5, 20, "CERRO VISTA"), WaterUsage(15, 4, 20, "SIERRA MADRE")], PCV
#Output Example: 149.0
#Structure: Create two variables to store total gallons and total dorm to divide total gallons by.
# Use for loop to cycle through the list of WaterUsage data and, if the housing data matches the inputted dorm name, grab the shower_time, sink_time, and toilet_flushes values from the data.
#Run each through their respective conversions, and add each to total gallons, and increase count of dorms by one. Divide total gallons by total dorms after loop is done, and return average gallons.
def general_average_water_usage(water: list[WaterUsage], dorm:str) -> float:
    total_gallons = 0
    total_dorms = 0
    for i in range(0, len(water)):
        if water[i].housing == dorm:
            shower_gallons = shower_water_conversion(water[i].shower_time)
            sink_gallons = sink_water_conversion(water[i].sink_time)
            flush_gallons = flushes_water_conversion(water[i].flushes)
            total_gallons += shower_gallons + sink_gallons + flush_gallons
            total_dorms += 1
    average_gallons = total_gallons / total_dorms
    return average_gallons

#Purpose: Updates the housing_average_dictionary with average gallons used by an input dorm in a day
#Input Type: dict, str, float
#Output Type: dict
#Example input: housing_average_dictionary, "PCV", 15
#Example Output: {"PCV": 15, "RED BRICKS": 0, "NORTH MOUNTAIN": 0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE": 0}
#Structure: Update values through dict[str] = value, then return the dictionary
def add_to_dictionary(dictionary: dict, key: str, value: float) -> dict:
    dictionary[key] = value
    return dictionary

#Purpose: Updates each dorm in the housing_average_dictionary with the average gallons of water used by the dorm based of WaterUsage data list.
#Input Type: list[WaterUsage]
#Output Type: None
#Example Input: [WaterUsage(45, 5, 10, "PCV"), WaterUsage(30, 4, 5, "RED BRICKS"), WaterUsage(20, 3, 10, "NORTH MOUNTAIN"), WaterUsage(15, 6, 15, "YAKITITU"), WaterUsage(20, 4, 15, "SIERRA MADRE"), WaterUsage(45, 5, 30, "CERRO VISTA"), WaterUsage(30, 4, 30, "PCV"), WaterUsage(10, 3, 5, "RED BRICKS"), WaterUsage(20, 6, 10, "NORTH MOUNTAIN"), WaterUsage(18, 3, 7, "YAKITITU"), WaterUsage(25, 5, 20, "CERRO VISTA"), WaterUsage(15, 4, 20, "SIERRA MADRE")]
#Example Output: None, but housing_average_dictionary becomes {"PCV": 149.0, "RED BRICKS": 69.75, "NORTH MOUNTAIN": 79.2, "YAKITUTU": 72.65, "CERRO VISTA": 150.5, "SIERRA MADRE": 88.65}
#Structure: for the number of keys in the dictionary, grab the key name and run it as well as the WaterUsage data list through general_average_water_usage and then add_to_dictionary to update dictionary.
def build_housing_averages(water_list: list[WaterUsage]) -> None:
    for dorm in Housing_average_dictionary.keys():
        avg = general_average_water_usage(water_list, dorm)
        add_to_dictionary(Housing_average_dictionary, dorm, avg)

#Purpose: Calculates average water usage based on dorm input name and user WaterUsage data.
#Input Type: WaterUsage
#Output Type: float
#Input Example: WaterUsage(9, 3, 10)
#Output Example: 49.3
#Structure: Create variable to store average gallons, and convert all WaterUsage data to gallons using conversion functions.
#Add up all gallons to get user gallon average.
def user_average_water_usage(water: WaterUsage) -> float:
    average_gallons = 0
    shower_gallons = shower_water_conversion(water.shower_time)
    sink_gallons = sink_water_conversion(water.sink_time)
    flush_gallons = flushes_water_conversion(water.flushes)
    average_gallons += shower_gallons + sink_gallons + flush_gallons
    return average_gallons

#Purpose: Looks through the housing_average_dictionary and finds the housing with the highest water usage.
#Input Type: dict
#Output Type: str
#Example Input: {"PCV": 149.0, "RED BRICKS": 69.75, "NORTH MOUNTAIN": 79.2, "YAKITUTU": 72.65, "CERRO VISTA": 150.5, "SIERRA MADRE": 88.65}
#Example Output: "CERRO VISTA"
#Structure: Cycle through the housing_average dictionary with a for loop, accessing both the key and quantity. Compare the quantity against the highest known value (initially 0).
#If the quantity is higher than the highest known quantity, update highest known quantity and update name of dorm with highest water usage. Return name of dorm with highest water usage.
def general_greatest_water_usage(water: dict) -> str:
    highest_water_dorm = ""
    max_gallons = 0
    for key, quantity in water.items():
        if quantity > max_gallons:
            max_gallons = quantity
            highest_water_dorm = key
    return highest_water_dorm

#Purpose: Compares a dorm's average from the housing-average-dictionary with a user's average water usage, and returns true if user's average is larger, false if not.
#Input Type: WaterUsage, str
#Output Type: bool
#Example Input: WaterUsage(9, 3, 10), PCV
#Example Output: False
#Structure: Get dorm average from housing_average_dictionary, as well as the user average by calculating through user_average_water_usage function.
#Compare values with if statement, and return true if user average is larger, return false if not.
def user_greatest_water_usage(user_data: WaterUsage, dorm: str) -> bool:
    dorm_average = Housing_average_dictionary[dorm]
    user_average = user_average_water_usage(user_data)
    if user_average > dorm_average:
        return True
    else:
        return False

#Purpose: Return a string with a recommendation for water usage based on user's data/water usage.
#Input Type: WaterUsage
#Output: str
#Example Input: WaterUsage(9, 3, 10)
#Example Output: "Good Work maintaining low water consumption, keep up what you are doing to help water conservation efforts.
#Structure:Get user water average by running user data through user average water usage function, and then use if statements to compare water usage.
#If water usage is less than or equal 60, return positive comment, else if less than or equal to 80, return statement to remind about water conservation.
#Else, return recommendations of reducing water usage.
def user_suggestions(user_data: WaterUsage) -> str:
    compare = user_average_water_usage(user_data)
    if compare <= 60:
        return "Good Work maintaining low water consumption, keep up what you are doing to help water conservation efforts!"
    elif compare <= 80:
        return "Good start on conservation, but you should still reduce your water usage by being more conscious of how much you use."
    else:
        return "Cut back on shower time, don't flush the toilet unnecessarily, and turn off the sink when you aren't using it to reduce your water usage and help our campus reduce its water waste."
