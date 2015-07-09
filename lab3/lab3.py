fd = open('users3.db', 'rb')
content = fd.read()
fd.close()

# How do you modify the content to satisfy the Oracle?
new_content = content

fd = open('users3_modified.db', 'wb+')
fd.write(sig + new_content)
fd.close()
