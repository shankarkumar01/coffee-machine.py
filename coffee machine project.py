# Coffee Machine OOP Project in Python
print("Program Started")
class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 500
        self.coffee = 300
        self.money = 0

        self.menu = {
            "espresso": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
                "cost": 80
            },
            "latte": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
                "cost": 120
            },
            "cappuccino": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
                "cost": 150
            }
        }

    def show_menu(self):
        print("\n----- MENU -----")
        for item, details in self.menu.items():
            print(f"{item.title()} - ₹{details['cost']}")

    def check_resources(self, drink):
        ingredients = self.menu[drink]

        if self.water < ingredients["water"]:
            print("Sorry, not enough water.")
            return False

        if self.milk < ingredients["milk"]:
            print("Sorry, not enough milk.")
            return False

        if self.coffee < ingredients["coffee"]:
            print("Sorry, not enough coffee.")
            return False

        return True

    def make_coffee(self, drink):
        ingredients = self.menu[drink]

        self.water -= ingredients["water"]
        self.milk -= ingredients["milk"]
        self.coffee -= ingredients["coffee"]
        self.money += ingredients["cost"]

        print(f"\nHere is your {drink}. Enjoy ☕")

    def report(self):
        print("\n----- MACHINE REPORT -----")
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ₹{self.money}")


# Main Program
machine = CoffeeMachine()

while True:
    print("\n1. Show Menu")
    print("2. Buy Coffee")
    print("3. Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        machine.show_menu()

    elif choice == "2":
        drink = input("Enter coffee name (espresso/latte/cappuccino): ").lower()

        if drink in machine.menu:
            if machine.check_resources(drink):
                machine.make_coffee(drink)
        else:
            print("Invalid coffee choice.")

    elif choice == "3":
        machine.report()

    elif choice == "4":
        print("Machine turned off.")
        break

    else:
        print("Invalid choice.")