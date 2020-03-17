import smtplib,unittest
from unittest import TestCase
from unittest.mock import Mock
from Sending_email import main
import logging

mock = Mock()
m = mock.Mock()
class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []
    
    def test_get_contacts(self,*args):
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = 'magdalene magdalene.selokela@umuzi.org'
        self.assertEqual(s.split(), ['magdalene','magdalene.selokela@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'magdalene.selokela@umuzi.org')
            self.assertEqual(s.emails[0].to, ['magdalene.selokela@gmail.com'])
            self.assertEqual(s.emails[0].msg, 'This is TEST')
            self.assertEqual(m.get_contacts) == False

    def tearDown(self):
        self.emails = None

if __name__ == '__main__':
    unittest.main()