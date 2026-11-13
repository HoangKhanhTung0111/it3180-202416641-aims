MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []
        
    def search_by_title(items, keyword):
        return [item for item in items if keyword.lower() in item.lower()]

    def print_cart(items):
        if not items:
            print("The cart is empty")
            return
        print("--- Your Cart ---")
        for item in items:
            print(item)

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print(f"The disc '{dvd.title}' has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)
    
    def get_discounted_total(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        total = self.total_cost()
        return total * (100 - percent) / 100


