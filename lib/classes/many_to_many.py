class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 < len(value) and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception('''Name must be a string and must be greater than or 
            equal to 3 in terms of length.  Once instantiated, name can't be changed.''')
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if 0 < len(self.orders()):
            return sum([order.price for order in self.orders()])/len(self.orders())
        else:
            return 0

class Customer:

    all = []

    def __init__(self, name):
        self.name = name

        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value
        else:
            raise Exception("Name must be a string and must be between 1 and 15 characters, inclusive.")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        best_customer = None
        most_spent = 0

        for cust in cls.all:
            temp_most = sum([order.price for order in coffee.orders() if order.customer == cust])
            if temp_most > most_spent:
                most_spent = temp_most
                best_customer = cust           

        return best_customer
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0 and not hasattr(self, "price"):
            self._price = value
        elif isinstance(value, int) and 1.0 <= value <= 10.0 and not hasattr(self, "price"):
            self._price = float(value)
        else:
            raise Exception('''Price must be of type float and my be between 1.0 and 10.0, inclusive.  
            It also can't be changed once instantiated.''')
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be of type Customer.")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be of type Coffee.")