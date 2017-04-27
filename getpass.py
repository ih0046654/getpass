#encoding:utf-8
from random import Random
import sys
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%&()<>?[]'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

if __name__ == '__main__':
	if int(len(sys.argv))<3:
		pwdlengh = int(sys.argv[1])
		print random_str(randomlength=pwdlengh)
	else:
		for i in range(int(sys.argv[2])):
			pwdlengh = int(sys.argv[1])
			print random_str(randomlength=pwdlengh)
