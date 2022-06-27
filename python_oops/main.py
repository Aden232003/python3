import csv

class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity):
        #run validations and recieve arguments
        #print(f"An instance created for : {name}")

        #assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # count out the floats that are point 0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"



class Phone(Item):
    def __init__(self,name: str,price: float,quantity, broken_phones = 0):
        #call the super function to access all attributes and methods 
        super().__init__(
            name, price, quantity
        )        
        #run validations and recieve arguments

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        #assign to self objects

        self.broken_phones = broken_phones



phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)

phone2 = Phone("jscPhonev20", 700, 5,1)