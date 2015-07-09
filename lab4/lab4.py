import subprocess
from subprocess import call

def test_database():
	output = subprocess.Popen("python lab4_oracle.pyc users4_modified.db", shell=True, stdout=subprocess.PIPE).stdout.read()

	if 'file is encrypted or is not a database' in output:
		return

	if 'Congratulations, you successfully passed this lab!' in output:
		print('You got it')
		exit(0)


fd = open(filename, 'rb')
content = fd.read()
fd.close()

# How to modify content?
content2 = content

fd = open('users4_modified.db', 'wb+')
fd.write(content2)
fd.close()

test_database()
