import unittest
from unittest.mock import patch
from notifier import send_telegram_alert

class TestNotifier(unittest.TestCase):
    @patch("notifier.requests.post")
    def test_send_alert_success(self, mock_post):
        mock_post.return_value.status_code = 200
        send_telegram_alert("Test message")
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
