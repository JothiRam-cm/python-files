import unittest
from validatecard import *

class credictcardvalidation (unittest.TestCase) :
    def setUp(self) :
        print("setUp method")
    def test_validationn_valid(self):
        result=validate(date(2023,12,31))
        self.assertEqual('valid',result)
        
    # def test_validationn_expired(self):
    #     result=validate(date(2022,12,31))
    #     self.assertEqual('Expired',result)
        
    def test_validationn_assert(self):
        self.assertRaises(RuntimeError)
        validate(date(2022,12,31))
    def tearDown(self) :
        print('tearDown method')   
        
if __name__ == '__main__' :
    unittest.main() 
