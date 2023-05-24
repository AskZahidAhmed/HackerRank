"""
 A valid email address meets the following criteria:
    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters.
    The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge. For example, this code:
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
produces this output:
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
"""

import email.utils
import re
n = int(input())
re_email = re.compile(r'^[A-Za-z][\w\.-]+@[A-Za-z]+\.[A-Za-z]{1,3}$')
for i in range(n):
    parse = email.utils.parseaddr(input())
    if re.fullmatch(re_email, parse[1]):
        print (email.utils.formataddr(parse))
