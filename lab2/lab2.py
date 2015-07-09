import base64
import sqlite3
import sys
from Crypto.PublicKey import RSA

public_key = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvVU6hQ7Uhly8qv6Z1N+T
h65pBHmQMdbm0sdW4YfhFyRQvkEQVRyLcJXYddqxA/4mvN+BIIzt2SnetUSD3in1
hOMZZnXFpAd71W8FlgLdALpY4BwiueW8s1RgvjjzzQ13V53aWqZ2AKMO7753yTE5
z01/YwjlBw/FICwIK3wwj3UCjIIOLTkqzNWnHXwXIC2geyDvYJVJdJvzx5uDDimP
l95villx0KwL6Cdqj5gpC4KeQP+KuwdHaMarya3x0M3ryM5acSe0M2NxpJAWDu1U
8PghFISfO39ORdIFCT8PeZS7YoT46ze2cHIYOSTbG+9brt/c0CZiKd0DljEwbHiY
7QIDAQAB
-----END PUBLIC KEY-----"""

# This function is. It is not really needed in this particular case

def getPermutations(chars, length, prefix=""):
	if length <= 1:
		for char in chars:
			yield prefix + char
	else:
		for char in chars:
			for perm in getPermutations(chars, length-1, prefix + char):
				yield perm

if len(sys.argv) != 2:
	print('Usage: python %s [database]' % sys.argv[0])
	print('')
	exit(0)

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()
c.execute("SELECT id, name, pin_cipher, pin_plain FROM User;")

rows = c.fetchall()

for row in rows:
	print(row)

c.close()
