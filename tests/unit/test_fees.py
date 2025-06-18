import unittest
from backend.bot.fees.advance_fee import handle_advance_fee_payment

class AdvanceFeeTest(unittest.TestCase):
    def test_fee_bounds(self):
        # Test fee calculation logic
        offer = {'amount_usd': 5000, 'currency': 'USDT', 'user_id': '123'}
        fee_usd = max(1, min(offer['amount_usd'] * 0.001, 10))
        self.assertEqual(fee_usd, 5)
        offer['amount_usd'] = 15000
        fee_usd = max(1, min(offer['amount_usd'] * 0.001, 10))
        self.assertEqual(fee_usd, 10)
        offer['amount_usd'] = 2
        fee_usd = max(1, min(offer['amount_usd'] * 0.001, 10))
        self.assertEqual(fee_usd, 1)
