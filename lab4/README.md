# Lab 4 - Breaking the integrity of SQLCipher

Python library required: [PySQLCipher](https://pypi.python.org/pypi/pysqlcipher)

Sqlcipher is a crypto library, available in multiple programming languages, which is encrypting a sqlite database. It is encrypting each 1024-byte page of the SQLite database independently.

The implementation in this lab made a critical mistake: they disabled MAC:

    db.execute('PRAGMA cipher_use_hmac = OFF;')

Your goal is to modify the database so that John12 has less than 10 actions.

For this, modify lab4.py and try multiple attempts, moving and/or copying some 1024 bytes pages around and see if the Oracle will accept the resulting database. You might want to automate the combinations as much as possible.
