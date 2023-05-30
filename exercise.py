class Store:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        dict1 = {'name': name,
                 'price': price}
        self.items.append(dict1)

    def stock_price(self,items):
        # Add together all item prices in self.items and return the total.
        total=0
        for item in items:
            total += sum(item['price'])
            return total

