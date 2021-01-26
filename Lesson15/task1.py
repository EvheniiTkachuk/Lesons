# Create a class method named `validate`, which should be called from the `__init__`
# method to validate parameter email, passed to the constructor. The logic inside
# the `validate` method could be to check if the passed email parameter is a valid email string.

from re import *


class CheckEmail:
    def __init__(self, email):
        self.email = CheckEmail.validate(email)

    @staticmethod
    def validate(email):
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        is_valid = pattern.match(email)
        return email if is_valid else False


address1 = 'developer@gmail.com'
address2 = 'developer'
address3 = 'developer^@gmail.com'

check = CheckEmail(address1)
print(f'{address1} - {bool(check.email)}')
check = CheckEmail(address2)
print(f'{address2} - {bool(check.email)}')
check = CheckEmail(address3)
print(f'{address3} - {bool(check.email)}')
