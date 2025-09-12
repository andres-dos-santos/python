import unittest

def sum(x, y):
  return x + y

class TestSum(unittest.TestCase):
  def test_sum_positive(self):
    self.assertEqual(sum(2, 4), 6)

  def test_sum_negative(self):
    self.assertEqual(sum(-1, 1), 0)
  
if __name__ == "__main__":
    unittest.main()