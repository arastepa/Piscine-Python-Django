from beverages import Capuccino, Chocolate, Coffee, HotBeverage, Tea
import random


class CoffeeMachine:
    def __init__(self):
        self.drinks = 0
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(0.90, "empty cup")
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.drinks = 0
        print("repairing")
    def serve(self, bevarrage: HotBeverage):
        if (self.drinks >= 10):
            raise CoffeeMachine.BrokenMachineException()
        self.drinks +=1
        res = random.randint(0, 5)
        if res == 2:
            return self.EmptyCup()   
        else:
            return bevarrage()

def main():
    machine = CoffeeMachine()
    bevarrages = [Coffee, Tea, Chocolate, Capuccino]
    for _ in range(0, 22):
        try:
            rand = random.randint(0, 3)
            print(machine.serve(bevarrages[rand]))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            machine.repair()

    

if __name__ == '__main__':
    main()