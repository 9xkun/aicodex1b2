import re

class ValidateString:
    PHONE_LENGTH_VN = 10

    @staticmethod
    def validate_email_format(email):
        email_regex = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]{2,3}$'
        return re.match(email_regex, email) is not None