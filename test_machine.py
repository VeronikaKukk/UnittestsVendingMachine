import unittest
from CoffeeMachine import CoffeeMachine, Latte, Americano, Iced_Coffee

class TestCoffeeMachine(unittest.TestCase):
    
    def test_getAvailableDrinks(self):
        # None, 1-2 drinks
        drinks = []
        machine = CoffeeMachine(drinks)
        self.assertEqual(machine.getAvailableDrinks(), drinks)
        
        drinks = [Iced_Coffee]
        machine = CoffeeMachine(drinks)
        self.assertEqual(machine.getAvailableDrinks(), drinks)
        
        drinks = [Latte, Americano]
        machine = CoffeeMachine(drinks)
        self.assertEqual(machine.getAvailableDrinks(), drinks)

    def test_orderDrink(self):
        machine = CoffeeMachine([Latte, Americano, Iced_Coffee])

        # Order a drink not in the machine
        money = 100.0
        self.assertEqual(machine.orderDrink("Milkshake", money), (None, money))

        # Order a drink in the machine
        money = 100.0
        drink_price = Americano().price
        self.assertEqual(machine.orderDrink("Americano", money), ("Americano", money - drink_price))
    
    def test_orderDrink_change(self):
        machine = CoffeeMachine([Americano])

        # Order a drink with exact money
        drink_price = Americano().price
        money = drink_price
        self.assertEqual(machine.orderDrink("Americano", money), ("Americano", money - drink_price))
        
        # Order a drink with more money
        money = drink_price + 2.0
        self.assertEqual(machine.orderDrink("Americano", money), ("Americano", money - drink_price))

        # Order a drink with less money
        money = drink_price - 2.0
        self.assertEqual(machine.orderDrink("Americano", money), (None, money))
        
        # Order a drink with incorrect money
        money = "this is money"
        self.assertEqual(machine.orderDrink("Americano", money), (None, money))

    def test_addSugar(self):
        machine = CoffeeMachine([Latte])

        # Adding sugar to invalid drink
        self.assertFalse(machine.addSugar())
        self.assertIsNone(machine.getCurrentDrink())
        
        # Adding sugar to valid drink
        drink_ingredients = Latte().getIngredients()
        drink_ingredients.append("Sugar")
        
        machine.orderDrink("Latte", 100.0)
        self.assertTrue(machine.addSugar())
        self.assertEqual(machine.getCurrentDrink().getIngredients(), drink_ingredients)

   
if __name__ == '__main__':
    unittest.main()