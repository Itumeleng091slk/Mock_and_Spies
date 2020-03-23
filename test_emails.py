import os
import smtplib,unittest
from unittest import TestCase
from unittest.mock import Mock
from Sending_email import main
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
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = "anonymous"
        self.assertEqual(s.split(), ['anonymous'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'anonymous')
            self.assertEqual(s.emails[0].to, ['anonymous'])
            self.assertEqual(s.emails[0].msg, 'This is TEST')
            self.assertEqual(m.get_contacts) == False

    def tearDown(self):
        self.emails = None

if __name__ == '__main__':
    unittest.main()
