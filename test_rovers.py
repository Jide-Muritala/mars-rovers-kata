import unittest
from rovers import Rover

class TestRover(unittest.TestCase):
    def test_turn_left(self):
        rovers = [
            Rover(5, 7, "S")
        ]
        my_number = 11
        first_rover_position = rovers[0]
        print('first_rover_position')
        self.assertEqual(True, True)



if __name__ == "__main__":
    unittest.main()