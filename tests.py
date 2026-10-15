import unittest
from credit_card_validator import credit_card_validator 

class TestCreditCardValidator(unittest.TestCase):
    
    def test_visa_card(self):
        """
        Verify that a valid Visa card returns True.
        Selected using Partition testing.
        """
        self.assertTrue(credit_card_validator('4234567891234567'))

    def test_visa_invalid_checksum(self):
        """
        Verify that an invalid Visa card returns False.
        Selected using Partition testing.
        """
        self.assertFalse(credit_card_validator('4234567891234568'))

    def test_visa_short_length(self):
        """
        Verify that a Visa number with an invalid length returns False.
        Selected using boundary value testing by choosing a length 
        one digit below required length.
        """
        self.assertFalse(credit_card_validator('423456789123456'))

    def test_visa_long_length(self):
        """
        Verify that a Visa number with an invalid length returns False.
        Selected using boundary value testing by choosing a length 
        one digit above required length.
        """
        self.assertFalse(credit_card_validator('42345678912345674'))








if __name__ == '__main__':
    unittest.main()