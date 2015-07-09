# Crypto Workshops - How to get around encryption

This series of labs show how to GET AROUND (not break, get around) popular encryption algorithms used every day when they are not properly implemented. The goal is to show how just using encryption is not enough, and to dispel some misconceptions. If strong cryptography is often a requirement for security, it is NOT enough.

THESE WORKSHOPS DO NOT REQUIRE MUCH KNOWLEDGE OF CRYPTOGRAPHY. You need to know what is symmetric encryption, asymmetric encryption, XOR'ing and a MAC.


### Misconception #1: data encrypted using a strong encryption algorithm is secure

The main misconception about cryptography is that, as long as something is encrypted using a known, strong algorithm, it is secure.

In practice, an attacker does not always need to be able to decrypt a ciphertext to be able to do some damage.

Consider the case of a so-called replay attack: you need to pay Bob $20, so you send your bank an electronic message asking it to pay Bob the sum of $20. The message contains your credentials (name, account number, password), and is encrypted using a super-secure algorithm. If Bob can eavesdrop on the network and get a copy of the message (or even intercept it), he cannot decrypt it, nor even modify it without your bank detecting the tampering.

But what if Bob sends again this same message to your bank 10 times? Unless a protection against a replay attack is in place, you would end up paying Bob $220 instead of $20.


### Misconception #2: cracking encryption is about decrypting the ciphertext

When we think about cracking encryption, we're generally thinking retrieving the full plaintext. Like in spy movies. This is not always the case.

Sometimes an attacker may only need to know a few characters, or even finds patterns in the ciphertext. Proper cryptography is not suppsoed to leak *any* information.

Also, cryptography doesn't also mean just protecting confidentiality. It also means protecting integrity. That is, making sure the ciphertext was not tampered with. Even without being able to decrypt the ciphertext, an attacker may be able to modify the ciphertext so that the plaintext will be modified in a certain way.

### [Lab 1 - Removing data without being caught](lab1/)
### [Lab 2 - Public key encryption of small plaintext is NOT secure](lab2/)
### [Lab 3 - Breaking the integrity of AES in CBC mode](lab3/)
### [Lab 4 - Breaking the integrity of sqlcipher](lab4/)


### Requirements

These labs were written using Python 2.7 with the [PyCrypto](https://www.dlitz.net/software/pycrypto/) library. Python is indeed a great language to manipulate text strings and binary data.

All labs are provided with a user database to crack and an Oracle that will display the content of the database as well as a message if you have successfully modified it (e.g. run `python lab1_oracle.pyc user1.db`)


### No cheating!

I am sure it is possible to reverse-engineer the Oracles (even though the keys you can see in the binary are NOT the keys applied), but you should not need that to pass the labs.
