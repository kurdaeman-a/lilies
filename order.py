class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.status = "Pending"

    def add_item(self, item_name, price):
        self.items.append({"item": item_name, "price": price})
        print(f"Added {item_name} to order.")

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def display_order(self):
        print(f"--- Order #{self.order_id} ---")
        print(f"Customer: {self.customer_name}")
        print("Items:")
        for item in self.items:
            print(f"  - {item['item']}: ${item['price']:.2f}")
        print(f"Total Price: ${self.calculate_total():.2f}")
        print(f"Status: {self.status}\n")

if __name__ == "__main__":
    my_order = Order(order_id=101, customer_name="Sarah")
    my_order.add_item("Matte Lipstick", 15.99)
    my_order.add_item("Vitamin C Serum", 24.50)
    my_order.display_order()