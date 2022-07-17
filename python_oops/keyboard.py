from item import Item

class Keyboard(Item):
    pay_rate = 0.5
    def __init__(self,name: str,price: float,quantity):
        #call the super function to access all attributes and methods 
        super().__init__(
            name, price, quantity
        )        