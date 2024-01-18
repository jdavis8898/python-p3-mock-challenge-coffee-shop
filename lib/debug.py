#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    coffee_1 = Coffee("Mocha")
    coffee_2 = Coffee("Vanilla Latte")
    customer = Customer("Steve")
    Order(customer, coffee_1, 2.0)
    Order(customer, coffee_1, 5.0)
    print(coffee_1.num_orders())

    ipdb.set_trace()
