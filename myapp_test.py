import unittest
import myapp

class TestMyApp(unittest.TestCase):

    def test_hi(self):
      self.assertEqual(myapp.say_hi(),'Hola soy Alexis')

if __name__=='__main__':
  unittest.main()
