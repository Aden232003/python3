from item import Item

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