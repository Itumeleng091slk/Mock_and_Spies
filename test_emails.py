import os
import smtplib,unittest
from unittest import TestCase
from unittest.mock import Mock
from mock import patch
from Sending_email import *
import logging

mock = Mock()
m = mock.Mock()
user = os.getenv("App_Address")
passwrd = os.getenv("App_Password")
to_email = os.getenv("App_email_to")

class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []
    
    def test_get_contacts(self,*args):
        for email in self.emails:
            self.assertTrue(email == main(),'Incorrect')
        sender = "anonymous"
        self.assertEqual(sender.split(), ['anonymous'])
        with self.assertRaises(TypeError):
            sender.split(2)
            self.assertEqual(len(sender.emails), 2)
            self.assertEqual(sender.emails[0].frm, 'anonymous')
            self.assertEqual(sender.emails[0].to, ['anonymous'])
            self.assertEqual(sender.emails[0].msg, 'Review project')
            self.assertEqual(mail.outbox[0].body, 'This is a test message sent to magdalene.selokela@gmail.com.')
            self.assertEqual(m.extract_contacts) == True

    def test_sending_mail(self,*args):
        with patch("smtplib.SMTP") as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            self.assertNotEqual('successful:email sent',Random_message("A verbal contract is not worth the paper it's written on.","Samuel Goldwyn")) == 404


if __name__ == '__main__':
    unittest.main()
