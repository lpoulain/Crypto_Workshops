# Lab 1: removing data without being caught

The Oracle lab1_oracle.pyc reads the content of an encrypted file users1.db and displays the access for some users.

You are told that the encryption used is pretty strong: it is using AES 128-bit in CBC mode for encryption and HMAC for integrity. Indeed, try to delete or replace one character and the Oracle will detect some issue.

But if you examine the ciphertext, you will find that even with a strong encryption used, some patterns can emerge. One weakness is that the encryption does not use any randomness, which leaks some information. But there are other weaknesses as well.

Your goal is to remove the "None" access for the user "gworkman" (and only this access) without the Oracle detecting any tampering.
