import unittest
from aminal_details import get_animals_details
class TestAnimal(unittest.TestCase):
    def test_no_animal(self):
        self.assertEqual(get_animals_details(None), 'No animal')
    
    def test_no_name(self):
        self.assertEqual(get_animals_details({ "type": "dog", "gender": "female" }), 'No animal name')
    
    def test_no_gender(self):
        self.assertEqual(get_animals_details({ "type": "dog", "name": "Lucy" }), 'No animal gender')
    
    def test_valid_animal(self):
        self.assertEqual(get_animals_details({ "type": "dog", "name": "Lucy", "gender": "female" }), 'Lucy is a female dog')
        
if __name__ == '__main__':
    unittest.main()