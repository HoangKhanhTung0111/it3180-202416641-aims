import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc  # Sửa lại đường dẫn import nếu file của bạn tên khác

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        
        # Thêm 20 đĩa đầu tiên -> Kỳ vọng đều trả về True (thành công)
        for i in range(20):
            dvd = DigitalVideoDisc(title=f"Movie {i+1}")
            self.assertTrue(cart.add_dvd(dvd))
            
        # Thêm đĩa thứ 21 -> Kỳ vọng trả về False (bị từ chối vì đầy giỏ)
        dvd_21 = DigitalVideoDisc(title="Movie 21")
        self.assertFalse(cart.add_dvd(dvd_21))
        
    def test_discount_calculation(self):
        cart = Cart()
        # Thêm 1 đĩa giá 100.0 vào cart ở đây (tùy theo hàm add của bạn)
        cart.add_dvd(DigitalVideoDisc(title="Test", cost=100.0))

        # Kiểm tra tính đúng tiền sau giảm: 100 giảm 20% = 80
        self.assertAlmostEqual(cart.get_discounted_total(20), 80.0)

        # Kiểm tra nhập phần trăm vô lý (150%) -> phải báo ValueError
        with self.assertRaises(ValueError):
            cart.get_discounted_total(150)
            
    def test_search_by_title_case_insensitive(self):
        d1 = DigitalVideoDisc(title="The Lion King", category="Animation", cost=19.95)
        result = search_by_title([d1], "lion")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")



if __name__ == "__main__":
    unittest.main()
