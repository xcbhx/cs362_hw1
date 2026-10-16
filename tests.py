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

    def test_mastercard_valid(self):
        """
        Verify that a valid MasterCard returns True.
        Selected using Partition testing.
        """
        self.assertTrue(credit_card_validator('5112345678912349'))

    def test_mastercard_upper_boundary(self):
        """
        Verify that a valid MasterCard with prefix 55 returns True.
        Selected using boundary value testing by using the
        upper boundary of the accepted prefix range (51-55).
        """
        self.assertTrue(credit_card_validator('5512345678912345'))

    def test_mastercard_lower_sec_prefix(self):
        """
        Verify that a valid MasterCard with prefix 2221 returns True.
        Selected using boundary value testing by using the
        lower boundary of the accepted prefix range (2221-2720).
        """
        self.assertTrue(credit_card_validator('2221345678912344'))

    def test_mastercard_upper_sec_prefix(self):
        """
        Verify that a valid MasterCard with prefix 2720 returns True.
        Selected using boundary value testing by using the
        upper boundary of the accepted prefix range (2221-2720).
        """
        self.assertTrue(credit_card_validator('2720345678912340'))

    def test_mastercard_invalid_lower_prefix(self):
        """
        Verify that an invalid MasterCard with prefix 50 returns False.
        Selected using boundary value testing by choosing
        one value below the accepted prefix range (51-55).
        """
        self.assertFalse(credit_card_validator('5034567891234566'))

    def test_mastercard_invalid_upper_prefix(self):
        """
        Verify that an invalid MasterCard with prefix 56 returns False.
        Selected using boundary value testing by choosing
        one value above the accepted prefix range (51-55).
        """
        self.assertFalse(credit_card_validator('5634567891234560'))

    def test_mastercard_invalid_lower_outbound(self):
        """
        Verify that an invalid MasterCard with prefix 2220 returns False.
        Selected using boundary value testing by choosing
        one value below the accepted prefix range (2221-2720).
        """
        self.assertFalse(credit_card_validator('2220567891234567'))

    def test_mastercard_invalid_upper_outbound(self):
        """
        Verify that an invalid MasterCard with prefix 2721 returns False.
        Selected using boundary value testing by choosing
        one value above the accepted prefix range (2221-2720).
        """
        self.assertFalse(credit_card_validator('2721567891234561'))

    def test_american_express_valid(self):
        """
        Verify that a valid American Express prefix 34 returns True.
        Selected using Partition testing.
        """
        self.assertTrue(credit_card_validator('341234567891232'))

    def test_american_express_upper_boundary(self):
        """
        Verify that a valid American Express with prefix 37 returns True.
        Selected using boundary value testing by using the
        upper boundary of the accepted prefix.
        """
        self.assertTrue(credit_card_validator('371234567891235'))

    def test_american_express_invalid_prefix_35(self):
        """
        Verify that an invalid American Express with prefix 35 returns False.
        Selected using partition testing by choosing an invalid prefix
        between the two accepted prefixes (34 and 37).
        """
        self.assertFalse(credit_card_validator('352056789123458'))

    def test_american_express_invalid_prefix_36(self):
        """
        Verify that an invalid American Express with prefix 36 returns False.
        Selected using partition testing by choosing an invalid prefix
        between the two accepted prefixes (34 and 37).
        """
        self.assertFalse(credit_card_validator('362156789123454'))

    def test_american_express_invalid_checksum(self):
        """
        Verify that an American Express card with an invalid
        Luhn checksum returns False.
        Selected using partition testing by choosing an
        invalid checksum with a valid prefix and length.
        """
        self.assertFalse(credit_card_validator('341234567891231'))

    def test_american_express_short_length(self):
        """
        Verify that an American Express with an invalid length returns False.
        Selected using boundary value testing by choosing a length
        one digit below required length.
        """
        self.assertFalse(credit_card_validator('34123456789122'))

    def test_american_express_long_length(self):
        """
        Verify that an American Express with an invalid length returns False.
        Selected using boundary value testing by choosing a length
        one digit above required length.
        """
        self.assertFalse(credit_card_validator('3712345678912314'))
    




if __name__ == '__main__':
    unittest.main()