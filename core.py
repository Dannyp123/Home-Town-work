class Topping:
    '''Represents a pizza topping.

    Each topping has a name and a price.
    For example, if pepperoni costs $0.75 to add to a pizza,
    you could represent that with Topping('Pepperoni', .75).

    Toppings are generally used to describe Pizzas.
    '''

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '{} (${:.2f})'.format(self.name, self.price)

    def __repr__(self):
        return 'Topping({},{})'.format(repr(self.name), repr(self.price))


class Side:
    '''Represents a side item.

    Each side item has a name and a price.
    '''

    def __init__(self, name, price):
        self.name = name
        self._price = price

    def price(self):
        return self._price

    def matches_name(self, name):
        '''(Side, String) -> Bool

        Return True if the provided name is a reasonable match for this item.
        The comparison is case insensitive.
        Providing an incomplete (starting) match works as well.

        >>> Side('Bread Sticks', 2).matches_name('bread')
        True
        >>> Side('Bread Sticks', 2).matches_name('Bread Sticks')
        True
        >>> Side('Bread Sticks', 2).matches_name('sticks')
        False
        '''
        return self.name.lower().startswith(name.lower())

    def __str__(self):
        return 'Side: {} (${:.2f})'.format(self.name, self.price())

    def __repr__(self):
        return 'Side({},{})'.format(repr(self.name), repr(self._price))


class Pizza:
    '''Represents a pizza.

    A pizza has a name, a list of toppings, and a base price of $7.

    For example a Pepperoni pizza could be represented as:

        Pizza('Pepperoni', [Topping('Pepperoni', .75)])

    A hawaiian pizza could be represented as:

        Pizza('Hawaiian', [Topping('Ham', .75), Topping('Pineapple', .5)])
    '''

    def __init__(self, name, toppings):
        self.name = name
        self.base_price = 7
        self.toppings = toppings

    def matches_name(self, name):
        '''(Pizza, String) -> Bool

        Return True if the provided name is a reasonable match for this item.
        The comparison is case insensitive.
        A suffix of ' Pizza' is ok.
        Providing an incomplete (starting) match works as well.

        >>> Pizza('Pepperoni', []).matches_name('Pepperoni')
        True
        >>> Pizza('Pepperoni', []).matches_name('pepperoni pizza')
        True
        >>> Pizza('Pepperoni', []).matches_name('pep')
        True
        >>> Pizza('Pepperoni', []).matches_name('epperoni')
        False
        '''
        return (self.name + ' pizza').lower().startswith(name.lower())

    def __str__(self):
        return '{} Pizza (${:.2f}){}'.format(
            self.name, self.price(),
            ''.join('\n    ' + str(t) for t in self.toppings))

    def price(self):
        return self.base_price + sum(t.price for t in self.toppings)

    def __repr__(self):
        return 'Pizza({},{})'.format(repr(self.name), repr(self.toppings))


class Order:
    '''Represents a customer's order.

    Each order has a customer's name and list of items being purchased.

    For example, if Base Camp Coding Academy was ordering two pepperoni pizzas,
    you could could represent it as:

        Order('Base Camp Coding Academy', [
            Pizza('Pepperoni', [Topping('Pepperoni', .75)]),
            Pizza('Pepperoni', [Topping('Pepperoni', .75)])
        ])
    '''

    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def total(self):
        return sum(i.price() for i in self.items)

    def add_item(self, item):
        '''(Order, (Pizza or Side)) -> None

        Adds the provided item to the order.

        >>> o = Order('cust name', [])
        >>> o.add_item(Side('Bread sticks', 1.5))
        >>> o.items
        [Side('Bread sticks',1.5)]
        '''
        self.items.append(item)

    def __str__(self):
        return 'Customer: {}\nTotal: ${:.2f}\nItems\n----------------{}'.format(
            self.customer, self.total(),
            ''.join('\n' + str(i) for i in self.items))

    def __repr__(self):
        return 'Order({},{})'.format(repr(self.customer), repr(self.items))


class Inventory:
    def __init__(self, pizzas, sides):
        self.pizzas = pizzas
        self.sides = sides

    def in_stock(self, name):
        '''(Inventory, String) -> Bool

        Returns True iff an item in stock matches the provided string.
        '''
        item = self.get_item(name)
        return not (item is None)

    def get_item(self, name):
        '''(Inventory, String) -> (Pizza or Side or None)

        Returns the first item (Pizza or Side) in the inventory that matches
        the provided name. If no item matches, None is returned.
        '''
        for item in self.pizzas + self.sides:
            if item.matches_name(name):
                return item

    def __str__(self):
        return 'Pizzas:\n{}\nSides:\n{}'.format(
            '\n'.join(map(str, self.pizzas)), '\n'.join(map(str, self.sides)))

    def __repr__(self):
        return 'Inventory({},{})'.format(repr(self.pizzas), repr(self.sides))
