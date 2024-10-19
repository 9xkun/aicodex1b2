import unittest
from app.utils.validate_string import ValidateString

class TestValidateEmail(unittest.TestCase):

    def test_validate_email_format_valid_email(self):
        self.assertTrue(ValidateString.validate_email_format('test@example.com'))

    def test_validate_email_format_invalid_email_no_at(self):
        self.assertFalse(ValidateString.validate_email_format('testexample.com'))

    def test_validate_email_format_invalid_email_no_domain(self):
        self.assertFalse(ValidateString.validate_email_format('test@.com'))

    def test_validate_email_format_invalid_email_special_chars(self):
        self.assertFalse(ValidateString.validate_email_format('test@exa!mple.com'))

    def test_validate_email_format_invalid_email_too_long_tld(self):
        self.assertFalse(ValidateString.validate_email_format('test@example.comm'))

    def test_validate_email_format_invalid_email_no_tld(self):
        self.assertFalse(ValidateString.validate_email_format('test@example'))