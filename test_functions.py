import functions
import unittest
import main
from main import WaterUsage

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
            WaterUsage(30, 4, 5, "Red Bricks"),
            WaterUsage(20, 3, 10, "North Mountain"),
            WaterUsage(15, 6, 15, "yakʔitʸutʸu"),
            WaterUsage(20, 4, 15, "Sierra Madre"),
            WaterUsage(45, 5, 30, "Cerro Vista"),
            WaterUsage(30, 4, 30, "PCV"),
            WaterUsage(10, 3, 5, "Red Bricks"),
            WaterUsage(20, 6, 10, "North Mountain"),
            WaterUsage(18, 3, 7, "yakʔitʸutʸu"),
            WaterUsage(25, 5, 20, "Cerro Vista"),
            WaterUsage(15, 4, 20, "Sierra Madre")
            ]
        input_element2 = "PCV"
        expected = 149.0
        result = functions.general_average_water_usage(input_element1, input_element2)
        self.assertEqual(expected, result)

    def test_general_average_water_usage2(self):
        input_element1 = [
            WaterUsage(45, 5, 10, "PCV"),
            WaterUsage(30, 4, 5, "Red Bricks"),
            WaterUsage(20, 3, 10, "North Mountain"),
            WaterUsage(15, 6, 15, "yakʔitʸutʸu"),
            WaterUsage(20, 4, 15, "Sierra Madre"),
            WaterUsage(45, 5, 30, "Cerro Vista"),
            WaterUsage(30, 4, 30, "PCV"),
            WaterUsage(10, 3, 5, "Red Bricks"),
            WaterUsage(20, 6, 10, "North Mountain"),
            WaterUsage(18, 3, 7, "yakʔitʸutʸu"),
            WaterUsage(25, 5, 20, "Cerro Vista"),
            WaterUsage(15, 4, 20, "Sierra Madre")
            ]
        input_element2 = "Red Bricks"
        expected = 69.75
        result = functions.general_average_water_usage(input_element1, input_element2)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
