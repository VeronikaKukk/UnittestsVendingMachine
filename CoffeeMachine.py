class CoffeeMachine:
    
    def __init__(self, available_drinks):
        self.drinks = available_drinks
        self.current_drink = None
    
    def getCurrentDrink(self):
        return self.current_drink
    
    def getAvailableDrinks(self):
        if len(self.drinks) == 0:
            print("No drinks available.")
        else:
            print("Available drinks are: ")
        for drink in self.drinks:
            print("\t" + drink.__name__.replace("_", " "))
        return self.drinks
    
    def orderDrink(self, drink_name, money):
        is_drink_found = False

        if len(drink_name) == 0:
            print("You need to enter a valid drink name.")
            return (None, money)
        if type(money) != float:
            print("Money has to be in float format.")
            return (None, money)
        
        for drink in self.drinks:
            if drink.__name__.replace("_", " ") == drink_name:
                is_drink_found = True
                wanted_drink = drink()
                if money >= wanted_drink.price:
                    self.current_drink = wanted_drink
                    change = round(money - self.current_drink.price, 2)
                    print("Money back: " + str(change))
                    return (self.current_drink.getName(), change)
                else:
                    print("Not enough money to buy " + drink_name + " for " + str(wanted_drink.price))
        
        if not is_drink_found:
            print(drink_name + " does not exist in this coffee machine.")

        return (None, money)
    

    def addSugar(self):
        if self.current_drink:
            self.current_drink.ingredients.append("Sugar")
            print("Sugar added to " + self.current_drink.name + ".")
            return True
        else:
            print("You have not ordered a drink yet.")
            return False


class Drink:
    
    def __init__(self, name, price, temperature, ingredients):
        self.name = name
        self.price = price
        self.temperature = temperature
        self.ingredients = ingredients
        
    def getIngredients(self):
        return self.ingredients
    
    def getPrice(self):
        return self.price
    
    def getTemperature(self):
        return self.temperature
    
    def getName(self):
        return self.name

class Latte(Drink):
    
    def __init__(self):
        super().__init__("Latte", 2.0, "Hot", ["Milk", "Espresso shot"])

class Iced_Coffee(Drink):
    
    def __init__(self):
        super().__init__("Iced Coffee", 3.15, "Cold", ["Milk", "Espresso shot", "Ice"])

class Americano(Drink):
    
    def __init__(self):
        super().__init__("Americano", 1.75, "Hot", ["Water", "Espresso shot"])
        
