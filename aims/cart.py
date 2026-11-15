MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []
        
    def search_by_category(discs, category):
        keyword = category.strip().lower()
        return [d for d in discs if keyword in d.category.lower()]
        
    def search_by_title(items, keyword):
        return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]


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
        print("Đã thêm đĩa vào giỏ hàng")
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
    
    def sort_by_title(self):
        # Sắp xếp tăng dần theo tên (title), nếu trùng tên thì sắp xếp giảm dần theo giá (cost)
        self.items.sort(key=lambda disc: (disc.title.lower(), -disc.cost))

    def sort_by_cost(self):
        # Sắp xếp giảm dần theo giá (cost), nếu trùng giá thì sắp xếp tăng dần theo tên (title)
        self.items.sort(key=lambda disc: (-disc.cost, disc.title.lower()))



