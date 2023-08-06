# Encryption Data

import hashlib
password = input("enter the password")
password = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(password)