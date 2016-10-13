"""Customers at Hackbright.

This provides a Customer class, helper methods to get all customers, find a
customer by email.

It reads customer data in from a text file.
"""

class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                first_name,
                last_name,
                email,
                password
                ):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convinience method to show information about customer in console"""

        return "<Customer: %s, %s, %s>" % (
            self.first_name, self.last_name, self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    # an empty dictionarry where we store our customer objects
    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                      last_name,
                                      email,
                                      password)

    return customers


    
def get_by_email(customer_email):
    """Return a customer, given its email."""
    return customers[customer_email]

# Dictionary to hold customers information.
#
# Format is {email: Customer object, ... }
customers = read_customers_from_file("customers.txt")