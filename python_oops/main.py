class Item:
    def __init__(self,name: str,price: float,qty):
        print(f"An instance created for : {name}")
        self.name = name
        self.price = price
        self.qty = qty
    def calculate_total_price(self, x,y):
        return x*y


#create attributes
item1 = Item("Phone",160,50)
item2 = Item("Laptop",140,100) 


