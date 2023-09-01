import unittest
# from esat import esat
# from humid import hitung_rh

def test_hitung_rh(self):
    self.assertEqual(self.hitung_rh(297,300), 83.7)
    self.assertEqual(self.hitung_rh(296,299), 83.5)

if __name__ == "__main__":
    unittest.main()