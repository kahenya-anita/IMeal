import unittest
from app.models import Meals

class Testmenu(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitches class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_food = Meals(1234,'Chapo','Flour, Water, Oil',20)

    def tearDown(self):

        '''
        Set up method that will run before every Test
        '''
        Meals.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_food,Meals))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_food.id,1234)
        self.assertEquals(self.new_food.name,'Chapo')
        self.assertEquals(self.new_food.ingredients,'Flour, Water, Oil')
        self.assertEquals(self.new_food.cost,20)
