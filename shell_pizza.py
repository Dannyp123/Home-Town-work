from core import *


def input_name():
    print('Welcome to hometown pizza!')
    name = input('What is the name for this order: ').title()
    return name


def get_inventory():
    inventory = Inventory([
        Pizza("Pepperoni", [Topping('pepperoni', .75)]),
        Pizza("Cheese", [Topping('cheese', .50)]),
        Pizza("Hawaiian", [Topping('Ham', 1.00),
                           Topping('Pineapple', .75)]),
        Pizza("Meat Lovers", [
            Topping('bacon', .50),
            Topping('ham', .25),
            Topping('sausage', .25)
        ])
    ], [
        Side('Breadsticks', 2.00),
        Side('2L Coke', 1.50),
        Side('Cinna Sticks', 2.50),
        Side('Sweet Tea', 7.50)
    ])
    return inventory


def ordering_food(name, inventory, order):
    while True:
        print('What would you like? ')
        print('If you are done ordering, enter done!')
        print('If you want to cancel your order, enter quit')
        choice = input('{}: '.format(name))
        if inventory.in_stock(choice):
            item = inventory.get_item(choice)
            order.add_item(item)
            print('Ok, 1 {} added to your order. Anything else?'.format(
                item.name))
            print()
        if choice == 'done':
            print('\nThank you for your business!')
            print('\nHave a blessed day!')
            print('\nHere is your receipt: ')
            print(order)
            break
        elif choice == 'quit':
            print('Have a blessed day!')
            quit()


def main():
    name = input_name()
    inventory = get_inventory()
    print()
    print(inventory)
    print()
    order = Order(name, [])
    print()
    ordering_food(name, inventory, order)


if __name__ == '__main__':
    main()
