import unittest
from detection import detect_log

class TestDetection(unittest.TestCase):
    def test_valid_failed_login(self):
        line = "Failed password for invalid user admin from 192.168.0.1 port 22 ssh2"
        result = detect_log(line)
        self.assertIsNotNone(result)
        self.assertEqual(result['username'], "admin")
        self.assertEqual(result['ip'], "192.168.0.1")
        self.assertTrue(result['invalid_user'])

    def test_invalid_line(self):
        line = "Accepted password for root from 192.168.0.2 port 22 ssh2"
        self.assertIsNone(detect_log(line))

if __name__ == "__main__":
    unittest.main()
