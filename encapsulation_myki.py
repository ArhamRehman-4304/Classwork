class Myki:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def top_up(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid top up amount")

    def make_trip(self, cost):
        if cost > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= cost
    
    def get_balance(self):
        return self.__balance
    
    def simulate_trip(self, cost=3.50):
        self.make_trip(cost)
        print(f"Trip cost: ${cost:.2f} / remaining balance: ${self.get_balance():.2f}")

    #creating objects (instances)

Myki_card1 = Myki("Alice", 20)

print(Myki_card1.owner)
print(Myki_card1.get_balance())
print(Myki_card1.simulate_trip())