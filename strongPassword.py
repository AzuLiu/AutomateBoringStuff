#regular expression
#Explanation:
# ^                         Start anchor
# (?=.*[A-Z].*[A-Z])        Ensure string has two uppercase letters.
# (?=.*[!@#$&*])            Ensure string has one special case letter.
# (?=.*[0-9].*[0-9])        Ensure string has two digits.
# (?=.*[a-z].*[a-z].*[a-z]) Ensure string has three lowercase letters.
# .{8}                      Ensure string is of length 8.
# $                         End anchor.

import re
strongPassword = re.compile(r'^(?=.*?[a-z])(?=.*?[A-z])(?=.*?[0-9]).{8,}$')
password = str(input('Password:'))
if strongPassword.search(password):
    print('Your password is strong.')
else:
    print('Your password is weak.')
