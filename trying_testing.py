import unittest

def multiply(a,b) -> int:
  return a * b

class TestMultiply(unittest.TestCase):

  def test_multiply(self):
    test_a = 5
    test_b = 10
    self.assertEqual(multiply(test_a, test_b), 50, "Should be 50")

if __name__ == "__main__":
  unittest.main()
