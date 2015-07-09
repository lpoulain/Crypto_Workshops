# Lab 4 - sqlcipher

Sqlcipher is a crypto library, available in multiple programming languages, which is encrypting a sqlite database.

Sqlcipher is encrypting each 1024 byte page independently.

The implementation here made a critical mistake: they disabled MAC:

    db.execute('PRAGMA cipher_use_hmac = OFF;')

Your goal is to modify the database so that John12 has less than 10 actions.

For this, modify lab4.py and try multiple attempts, moving some 1024 bytes pages around and see if the Oracle will accept the resulting database.
