# Lab 2: Public key encryption of small plaintext is NOT secure

Python library required: [PyCrypto](https://www.dlitz.net/software/pycrypto/)

One of the recommentations of the [OWASP top 10 most critical web application security risks](http://owasptop10.googlecode.com/files/OWASP%20Top%2010%20-%202013.pdf) (A6 - Sensitive Data Exposure) is to encrypt sensitive data such as credit card number with a public key, and only provide backend application with the private key. As a result, if the website gets compromised, attackers cannot decrypt that sensitive data - only backend applications can.

If asymmetric encryption (i.e. with a public and a private key scheme) is a great encryption scheme, it is NOT a safe scheme for encrypting small amounts of data.

## The lab

The lab contains a sqlite database users2.db which contains a list of users and a 5-digit PIN number encrypted using a 2048-bit asymmetric key scheme. You are provided with the public key.

The Oracle, which has the private key, will read the database and check whether the encrypted PIN (pin_cipher field) matches the plaintext PIN (pin_plain field, which is blank right now). Your job is to modify `lab2.py` to modify the database (or a copy), filling in the pin_plain field so that the Oracle OKs the plaintext PIN for all the users.

**Tips**

If brute-forcing the private key is unfeasible, you can easily brute-force the PIN!

Implement these three algorithms to pass this lab:

1. Use the PyCrypto library [Crypto.PublicKey.RSA class](https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html) to encrypt all 100,000 PIN possibilities and store the (ciphertext -> plaintext) results in a dictionary (`lab2.py` contains the public key). You can then quickly decrypt each user's PIN by performing a dictionary lookup. This is the fastest method when you have several users.
2. Brute-force each record independantly. This is slower but works even if the encrypted data is salted(*) - as long as you know how the salt is applied
3. Brute-force the first record, determine the value for pin_plain and then copy the pin_cipher and pin_plain to all the other records. Some might consider this as cheating, but this method might work in some circumstances.

## Food for thoughts

Consider other types of plaintext that could be easily broken. U.S. Social Security numbers would take longer to crack, but it is not an impossible task (9 digits, so 1 billion possibilities). Even credit card numbers may be at risk if storing only the 16 digits number. These numbers are indeed not uniform. The first digits are indeed specific to the issuer (and the number might be limited).

<br>

<sup>(*) A salt is some random data which is appended to the plaintext to avoid that two records with the same plaintext have the same ciphertext. This salt is typically stored in a field on the record</sup>
