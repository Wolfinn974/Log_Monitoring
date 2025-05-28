import unittest
import time
from rate_limit import RateLimiter
from unittest.mock import patch

class TestRateLimiter(unittest.TestCase):
    def test_block_after_limit(self):
        limiter = RateLimiter(max_attempts=3, window_seconds=1)
        ip = "1.2.3.4"

        for _ in range(2):
            self.assertFalse(limiter.register_attempt(ip))

        self.assertTrue(limiter.register_attempt(ip))

    def test_reset_after_window(self):
        limiter = RateLimiter(max_attempts=3, window_seconds=5)
        ip = "192.168.0.1"

        with patch("time.time") as mock_time:
            mock_time.return_value = 1000
            limiter.register_attempt(ip)
            limiter.register_attempt(ip)
            limiter.register_attempt(ip)
            self.assertTrue(limiter.ip_blocked(ip))

            # Simuler passage de temps après la fenêtre
            mock_time.return_value = 1006  # +6s après
            limiter.register_attempt(ip)
            self.assertFalse(limiter.ip_blocked(ip))
        
if __name__ == "__main__":
    unittest.main()
