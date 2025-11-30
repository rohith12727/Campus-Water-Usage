from classes import WaterUsage
import data

Housing_average_dictionary = {"PCV": 0, "RED BRICKS": 0, "NORTH MOUNTAIN": 0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE / YOSEMITE": 0}

def shower_water_conversion(minutes: float) -> float:
    gallons = round(minutes * 2.5, 3)
    return gallons

def sink_water_conversion(minutes: float) -> float:
    gallons = round(minutes * 2.2, 3)
    return gallons

def flushes_water_conversion(flushes: float) -> float:
    gallons = round(flushes * 1.6, 3)
    return gallons

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

def add_to_dictionary(dictionary: dict, key: str, value: float) -> dict:
    dictionary[key] = value
    return dictionary

def build_housing_averages(water_list: list[WaterUsage]) -> None:
    dorms = ["PCV", "RED BRICKS", "NORTH MOUNTAIN", "YAKITITU", "CERRO VISTA", "SIERRA MADRE"]
    for dorm in dorms:
        avg = general_average_water_usage(water_list, dorm)
        add_to_dictionary(Housing_average_dictionary, dorm, avg)

def user_average_water_usage(water: WaterUsage) -> float:
    average_gallons = 0
    shower_gallons = shower_water_conversion(water.shower_time)
    sink_gallons = sink_water_conversion(water.sink_time)
    flush_gallons = flushes_water_conversion(water.flushes)
    average_gallons += shower_gallons + sink_gallons + flush_gallons
    return average_gallons

def general_greatest_water_usage(water: dict) -> str:
    highest_water_dorm = ""
    max_gallons = 0
    for key, quantity in water.items():
        if quantity > max_gallons:
            max_gallons = quantity
            highest_water_dorm = key
    return highest_water_dorm

def user_greatest_water_usage(user_data: WaterUsage, dorm: str) -> bool:
    dorm_average = Housing_average_dictionary[dorm]
    user_average = user_average_water_usage(user_data)
    if user_average > dorm_average:
        return True
    else:
        return False

def user_suggestions(user_data: WaterUsage) -> str:
    compare = user_average_water_usage(user_data)
    if compare <= 60:
        return "Good Work maintaining low water consumption, keep up what you are doing to help water conservation efforts!"
    elif compare <= 80:
        return "Good start, but you should still reduce your water usage by being more conscious of how much you use."
    else:
        return "Cut back on shower time, don't flush the toilet unnecessarily, and turn off the sink when you aren't using it to reduce your water usage and help our campus reduce its water waste."
