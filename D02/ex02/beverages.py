class HotBeverage:
    def __init__(self, price = 0.30, name = "hot bevarage"):
        self.price = price
        self.name = name
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return f'''
            name: {self.name}
            price: {self.price:.2f}
            description: {self.description()}
        '''
    
class Coffee(HotBeverage):
    def __init__(self, price = 0.40, name = 'coffee'):
        super().__init__(price, name)
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self, price = 0.30, name = 'tea'):
        super().__init__(price, name)
    def desciption(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self, price = 0.50, name = 'chocoalte'):
        super().__init__(price, name)
    def description(self):
        return "Chocolate, sweet chocolate..."
class Capuccino(HotBeverage):
    def __init__(self, price = 0.45, name = 'capuccino'):
        super().__init__(price, name)
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

def run():
    beverage = HotBeverage()
    print(beverage)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    chocolate = Chocolate()
    print(chocolate)
    capuccino = Capuccino()
    print(capuccino)



if __name__ == '__main__':
    run()