#!usr/bin/env python
#-*- coding:utf-8 -*-


def DealKey(key,omit):

	result = ''

	key = key.lower()

	for i in key:

		if i.isalpha() and i != omit and result.find(i) == -1:

				result = result + i

	if len(result) < 25:

		for i in range(97,123):

			if chr(i) != omit and result.find(chr(i)) != -1:

					result = result + chr(i)

	return result

def ImportKeyRow(keys):

	Arr = [[] for i in range(5)]

	m = 0

	n = 0

	for key in keys:

		Arr[m].append(key)

		n = n + 1

		if n == 5:

			m = m + 1

			n = 0

	for a in Arr:

		print a

	return Arr

def ImportKeyCol(keys):

	Arr = [[] for i in range(5)]

	m = 0

	for key in keys:

		Arr[m].append(key)

		m = m + 1

		if m == 5:

			m = 0

	for a in Arr:

		print a

	return Arr



def DealPw(pw):

	pw = pw.replace(' ','')

	pw = pw.lower()

	pw = pw.replace('q','')

	if not pw.isalpha():

		exit(0)

	if len(pw)%2 != 0:

		print 'It is not a even Number'

		pw = pw + 'x'

	result = []

	for i in range(len(pw)/2):

		result.append(pw[i*2:(i+1)*2])

	return result

def Locate(key,word):


	if word == 'j':

		word = 'i'

	for everyLine in range(len(key)):

		if key[everyLine].count(word) == 1:

			for everyColmn in range(len(key[everyLine])):

				if key[everyLine][everyColmn] == word:

					return str(everyLine),(everyColmn)


def Move(location):

	if location > 0:

		location = location - 1

	else:

		location = 4


	return str(location)


def exploit(key,pw):

	result = ''

	for i in pw: 

		x1,y1 = Locate(key,i[0])

		x2,y2 = Locate(key,i[1])

		if y1 == y2:

			x1 = Move(int(x1))

			x2 = Move(int(x2))

			result = result + key[int(x1)][int(y1)] + key[int(x2)][int(y2)]

		elif x1 == x2:

			y1 = Move(int(y1))

			y2 = Move(int(y2))

			result = result + key[int(x1)][int(y1)] + key[int(x2)][int(y2)]

		else:

			x3,y3 = x2,y1

			x4,y4 = x1,y2

			result = result + key[int(x4)][int(y4)] + key[int(x3)][int(y3)]

	print result


def main():


	key = raw_input('Input the key:')

	key = key.replace(' ','')

	omit = raw_input('Imput the omit:')

	key = DealKey(key,omit)

	key = ImportKeyRow(key)

	pw = raw_input('Input your passwd:')

	pw = pw.replace(' ','')

	pw = DealPw(pw)

	exploit(key,pw)



if __name__ == '__main__':

	main()





'''
def DealKey(key):

	result = ''

	for i in key:

		if i.isalpha():

			if i == 'j':

				i = 'i'

			if result.find(i) == -1:

				result = result + i

	if len(result) < 25:

		for i in range(97,123):

			if chr(i) != 'j' and result.find(chr(i)) == -1:

				result = result + chr(i)

	return result


def EncrptPw(pw):

	if not pw.isalpha():

		print 'Only letter!'

		exit(0)

	pw = pw.lower()

	result = ''

	if len(pw)%2 != 0:

		lenght = (len(pw)+1)/2

	else:

		lenght = len(pw)/2

	for i in range(lenght):

		get = pw[i*2:(i+1)*2]

		if len(get) == 2:

			if get[0:1] != get[1:2]:

				result = result + get

			else:

				result = result + get[0:1] + 'x' + get[1:2] + 'x'

		else:

			result = result + get[0:1] + 'x'

	print result

'''