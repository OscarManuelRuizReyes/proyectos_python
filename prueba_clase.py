# Elaboracion de programa de cafetera con clases

class coffe:
    def __init__(self, water, milk, cofee_beans, disponsable_cups, money):
        self.water = water
        self.milk = milk
        self.cofee_beans = cofee_beans
        self.disponsable_cups = disponsable_cups
        self.money = money

    def es_suficiente(self, cur_water, cur_mill, cur_cofee, cur_cups):
        if cur_water > self.water:
            print("Sorry, not enough water!")
        elif cur_mill > self.milk:
            print("Sorry, not enough milk!")
        elif cur_cofee > self.cofee_beans:
            print("Sorry, not enough cofee beans!")
        elif cur_cups > self.disponsable_cups:
            print("Sorry, not enough disponsable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            return 1

    def print_state(self):
        print()
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.cofee_beans))
        print("{} of disposable cups".format(self.disponsable_cups))
        print("${} of money".format(self.money))
        print()

    def buy_coffe(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        op = input()
        if op == "back":
            print()
            return
        op = int(op)
        if op == 1:
            if self.es_suficiente(250, 16, 0, 1):
                self.water -= 250
                self.cofee_beans -= 16
                self.money += 4
                self.disponsable_cups -= 1
        elif op == 2:
            if self.es_suficiente(350, 75, 20, 1):
                self.water -= 350
                self.milk -= 75
                self.cofee_beans -= 20
                self.money += 7
                self.disponsable_cups -= 1
        elif op == 3:
            if self.es_suficiente(250, 100, 12, 1):
                self.water -= 200
                self.milk -= 100
                self.cofee_beans -= 12
                self.money += 6
                self.disponsable_cups -= 1
        print()

    def take_money(self):
        print()
        print("I gave you ${}".format(self.money))
        self.money = 0
        print()

    def fill_coffe(self):
        print()
        print("Write how many ml of water do you want to add:")
        inc_water = int(input())
        self.water = self.water + inc_water
        print("Write how many ml of milk do you want to add:")
        inc_milk = int(input())
        self.milk = self.milk + inc_milk
        print("Write how many grams of coffee beans do you want to add:")
        inc_grams = int(input())
        self.cofee_beans = self.cofee_beans + inc_grams
        print("Write how many disposable cups of coffee do you want to add:")
        inc_cups = int(input())
        self.disponsable_cups = self.disponsable_cups + inc_cups
        print()

    def main(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "buy":
                self.buy_coffe()
            elif action == "fill":
                self.fill_coffe()
            elif action == "take":
                self.take_money()
            elif action == "remaining":
                self.print_state()
            elif action == "exit":
                break


cafe = coffe(400, 540, 120, 9, 550)
cafe.main()









