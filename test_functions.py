import functions
import unittest
from classes import WaterUsage

housing_average_dictionary = {"PCV": 149.0, "RED BRICKS": 69.75, "NORTH MOUNTAIN": 79.2, "YAKITUTU": 72.65, "CERRO VISTA": 150.5, "SIERRA MADRE": 88.65}
test_dictionary = {"PCV": 0, "RED BRICKS": 0, "NORTH MOUNTAIN": 0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE": 0}
class TestCases(unittest.TestCase):

#test_shower_water_conversion
    def test_shower_water_conversion(self):
        input_element = 5
        expected = 12.5
        result = functions.shower_water_conversion(input_element)
        self.assertEqual(expected, result)

    def test_shower_water_conversion2(self):
        input_element = 7.7
        expected = 19.25
        result = functions.shower_water_conversion(input_element)
        self.assertEqual(expected, result)
#test_sink_water_conversion
    def test_shower_sink_conversion(self):
        input_element = 5.5
        expected = 12.1
        result = functions.sink_water_conversion(input_element)
        self.assertEqual(expected, result)

    def test_shower_sink_conversion2(self):
        input_element = 20
        expected = 44.0
        result = functions.sink_water_conversion(input_element)
        self.assertEqual(expected, result)
#test_flushes_water_conversion
    def test_flushes_water_conversion(self):
        input_element = 6
        expected = 9.6
        result = functions.flushes_water_conversion(input_element)
        self.assertEqual(expected, result)

    def test_flushes_water_conversion2(self):
        input_element = 4
        expected = 6.4
        result = functions.flushes_water_conversion(input_element)
        self.assertEqual(expected, result)
#test_general_average_water_usage
    def test_general_average_water_usage(self):
        input_element1 = [
            WaterUsage(45, 5, 10, "PCV"),
            WaterUsage(30, 4, 5, "RED BRICKS"),
            WaterUsage(20, 3, 10, "NORTH MOUNTAIN"),
            WaterUsage(15, 6, 15, "YAKITITU"),
            WaterUsage(20, 4, 15, "SIERRA MADRE"),
            WaterUsage(45, 5, 30, "CERRO VISTA"),
            WaterUsage(30, 4, 30, "PCV"),
            WaterUsage(10, 3, 5, "RED BRICKS"),
            WaterUsage(20, 6, 10, "NORTH MOUNTAIN"),
            WaterUsage(18, 3, 7, "YAKITITU"),
            WaterUsage(25, 5, 20, "CERRO VISTA"),
            WaterUsage(15, 4, 20, "SIERRA MADRE")
            ]
        input_element2 = "PCV"
        expected = 149.0
        result = functions.general_average_water_usage(input_element1, input_element2)
        self.assertEqual(expected, result)

    def test_general_average_water_usage2(self):
        input_element1 = [
            WaterUsage(45, 5, 10, "PCV"),
            WaterUsage(30, 4, 5, "RED BRICKS"),
            WaterUsage(20, 3, 10, "NORTH MOUNTAIN"),
            WaterUsage(15, 6, 15, "YAKITUTU"),
            WaterUsage(20, 4, 15, "SIERRA MADRE"),
            WaterUsage(45, 5, 30, "CERRO VISTA"),
            WaterUsage(30, 4, 30, "PCV"),
            WaterUsage(10, 3, 5, "RED BRICKS"),
            WaterUsage(20, 6, 10, "NORTH MOUNTAIN"),
            WaterUsage(18, 3, 7, "YAKITUTU"),
            WaterUsage(25, 5, 20, "CERRO VISTA"),
            WaterUsage(15, 4, 20, "SIERRA MADRE")
            ]
        input_element2 = "Red Bricks"
        expected = 69.75
        result = functions.general_average_water_usage(input_element1, input_element2)
        self.assertEqual(expected, result)

    def test_add_to_dictionary(self):
        input = test_dictionary
        result = functions.add_to_dictionary(input, "PCV", 80.0)
        expected = {"PCV": 80.0, "RED BRICKS": 0, "NORTH MOUNTAIN": 0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE": 0}
        self.assertEqual(expected, result)

    def test_add_to_dictionary_2(self):
        input = test_dictionary
        result = functions.add_to_dictionary(input, "NORTH MOUNTAIN", 78.0)
        expected = {"PCV": 0, "RED BRICKS": 0, "NORTH MOUNTAIN": 78.0, "YAKITUTU": 0, "CERRO VISTA": 0, "SIERRA MADRE": 0}
        self.assertEqual(expected, result)

    def test_user_average_water_usage(self):
        input = WaterUsage(9, 3, 10, "PCV")
        result = functions.user_average_water_usage(input)
        expected = 49.3
        self.assertEqual(expected, result)

    def test_user_average_water_usage2(self):
        input = WaterUsage(40, 3, 15, "RED BRICKS")
        result = functions.user_average_water_usage(input)
        expected = 137.8
        self.assertEqual(expected, result)

    def test_general_greatest_water_usage(self):
        input = housing_average_dictionary
        result = functions.general_greatest_water_usage(input)
        expected = "CERRO VISTA"
        self.assertEqual(expected, result)

    def test_general_greatest_water_usage2(self):
        input = {"PCV": 149.0, "RED BRICKS": 69.75, "NORTH MOUNTAIN": 179.2, "YAKITUTU": 72.65, "CERRO VISTA": 150.5, "SIERRA MADRE": 88.65}
        result = functions.general_greatest_water_usage(input)
        expected = "NORTH MOUNTAIN"
        self.assertEqual(expected, result)

    def test_user_greatest_water_usage(self):
        input = WaterUsage(9, 3, 10, "PCV")
        result = functions.user_greatest_water_usage(input, "PCV")
        expected = True
        self.assertEqual(expected, result)

    def test_user_greatest_water_usage2(self):
        input = WaterUsage(0, 0, 0, "RED BRICKS")
        result = functions.user_greatest_water_usage(input, "RED BRICKS")
        expected = False
        self.assertEqual(expected, result)

    def test_user_suggestions(self):
        input = WaterUsage(9, 3, 10, "RED BRICKS")
        result = functions.user_suggestions(input)
        expected = "Good Work maintaining low water consumption, keep up what you are doing to help water conservation efforts!"
        self.assertEqual(expected, result)

    def test_user_suggestions2(self):
        input = WaterUsage(23, 3, 50, "RED BRICKS")
        result = functions.user_suggestions(input)
        expected = "Cut back on shower time, don't flush the toilet unnecessarily, and turn off the sink when you aren't using it to reduce your water usage and help our campus reduce its water waste."
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
