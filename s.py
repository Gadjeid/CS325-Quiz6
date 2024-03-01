class OrderDetails:
    def __init__(self, customer_info, address):
        self.items = []
        self.customer_info = customer_info
        self.address = address

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name, amount):
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] -= amount
                if item['quantity'] <= 0:
                    self.items.remove(item)
    def get_items(self):
        return self.items

class PriceCalculator:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.discount = 0

    def set_discount(self, discount):
        self.discount = discount

    def calculate_order_cost(self, items):
        subtotal = sum(item['price'] * item['quantity'] for item in items)
        subtotal += subtotal * self.tax_rate / 100
        subtotal -= subtotal * self.discount / 100
        return subtotal
    
class OrderVerify:
    def validate(self, items, customer_address):
        for item in items:
            if item['quantity'] > item['available_quantity']:
                raise Exception(f"{item['name']} is not available in that quantity, only {item['available_quantity']} is available")
                                
        if not customer_address:
            raise Exception("Customer address is not provided")

class OrderEmailConfirmation:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def send_confirmation_email(self, email):
        # self.email_service.send_email(email, "Order Confirmation")
        # Some implementation of email to user
        print(f"Order confirmation email sent to {email}.")

class InventoryUpdate:
    def update_inventory(self, items):
        for item in items:
            item['available_quantity'] -= item['quantity']


class Order:
    def __init__(self, customer_info, shipping_address):
        self.details = OrderDetails(customer_info, shipping_address)
        self.calc_cost = PriceCalculator(4.95)
        self.validator = OrderVerify()
        self.email_confirm = OrderEmailConfirmation('gmail')
        self.inventory_updater = InventoryUpdate()

    def add_to_cart(self, items):
        for item in items:
            if item['available_quantity'] > 0:
                self.details.add_item(item)

    def remove_from_cart(self, item_name, amount):
        self.details.remove_item(item_name, amount)
    
    def get_cart_items(self):
        return self.details.get_items()
    
    def discount(self, discount):
        self.calc_cost.set_discount(discount)

    def get_cart_cost(self):
        return self.calc_cost.calculate_order_cost(self.details.items)
    
    def process_order(self):
        self.validator.validate(self.details.items, self.details.address)
        total = self.calc_cost.calculate_order_cost(self.details.items)
        self.email_confirm.send_confirmation_email(self.details.customer_info['email'])
        self.inventory_updater.update_inventory(self.details.items)
        self.details.items.clear()
        return total

def main():
    items = [
        {'name': 'Book', 'price': 14.23, 'quantity': 2, 'available_quantity': 10},
        {'name': 'Apple', 'price': 2.23, 'quantity': 6, 'available_quantity': 6},
        {'name': 'Pencil', 'price': 0.84, 'quantity': 6, 'available_quantity': 12}
    ]
    
    customer_info = {
        'name': 'Emilie De Rochefort',
        'email': 'lilirochefort@example.com'
    }

    shipping_address = '99 Boulevard du Jardin Exotique, Jardin Exotique, Monaco'

    order = Order(customer_info, shipping_address)
    order.add_to_cart(items)
    order.discount(15)
    cart = order.get_cart_items()
    subtotal = order.get_cart_cost()
    
    print("Cart: ")
    for cart_item in cart:
        print(cart_item)
    print(f"Cart Total: {subtotal:.{2}f}")

    print("\nProcessing Order...")
    final_total = order.process_order()
    print(f"Total cost: {final_total:.{2}f}")

    cart = order.get_cart_items()
    subtotal = order.get_cart_cost()
    print("\nCart: ")
    for cart_item in cart:
        print(cart_item)
    print(f"Cart Total: {subtotal:.{2}f}")


if __name__=='__main__':
    main()