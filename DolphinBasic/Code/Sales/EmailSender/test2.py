import unittest
from unittest.mock import patch, MagicMock
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from emai_sender_2 import send_emails


class TestEmailSender(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_send_emails(self, mock_smtp):
        # Create a mock SMTP instance with a successful sendmail return
        instance = mock_smtp.return_value
        instance.sendmail.return_value = {}

        email_body = "This is a test email."
        try:
            send_emails(email_body)
            result = True
        except:
            result = False
        self.assertTrue(result)

        # Check if the SMTP instance was used correctly
        mock_smtp.assert_called_once_with("smtp.mycompany.com", 587)
        instance.starttls.assert_called_once()
        instance.sendmail.assert_called_once()


if __name__ == "__main__":
    unittest.main()
