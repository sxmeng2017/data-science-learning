import unittest

class MyTest(unittest.TestCase):
    def tearDown(self):
        print('finish')
        
    def setUp(self):
        print('set up')
        
    @classmethod
    def tearDownClass(self):
        print('class is over')
    
    @classmethod
    def setUpClass(self):
        print('class is running')
    
    def test_a_run(self):
        self.assertEqual(1,1)
    
    def test_b_run(self):
        self.assertEqual(2,2)
if __name__ == '__main__':
    unittest.main()
