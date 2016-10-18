#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''

'''
from numpy import *

from optparse import OptionParser

def Start():

	opt = OptionParser()

	opt.add_option('-k',dest='key',help="Input your matrix")

	opt.add_option('-p',dest='pw',help="Input your passwd")

	options,args = opt.parse_args()

	if options.pw is None or options.key is None:

		print 'Use \'-h\' to get help'

		exit(0)

	return options

def ForKey(key):

	key = mat(key)

	key = key.I.T

	print 'key is :'

	print key

	print '------------------------------------------'

	return key

def ForPw(pw,lenght):

	result = [[] for i in range(len(pw)/lenght)]

	for i in range(len(pw)/lenght):

		string = pw[i*lenght:(i+1)*lenght]

		for s in string:

			if s.isalpha():

				s = ord(s) - 96

			result[i].append(s)

	result = mat(result)

	print 'password matrix is:' 

	print result

	print '------------------------------------------'

	return result

def Deal(start):

	key = start.key

	pw = start.pw

	if pw.isalpha():

		judge = True

	key = ForKey(key)

	result = ForPw(pw,len(key))

	return key,result,judge

def Exploit(key,result,judge):

	get = result * key

	print 'The result matrix is:'

	print get

	print '------------------------------------------'

	get = array(get)

	string = ''

	for n in get:

		for i in n:

			one = int(i)

			while one < 0:
				
				one = one + 26

			one = one + 96

			string = string + chr(one)

	print 'The final result is:\n' + string


def main():

	start = Start()

	key,result,judge = Deal(start)

	Exploit(key,result,judge)

if __name__ == '__main__':

	main()

'''

Usage:

python Hill.py -k '1,2;0,1' -p dloguszijluswogany
key is :
[[ 1.  0.]
 [-2.  1.]]
------------------------------------------
password matrix is:
[[ 4 12]
 [15  7]
 [21 19]
 [26  9]
 [10 12]
 [21 19]
 [23 15]
 [ 7  1]
 [14 25]]
------------------------------------------
The result matrix is:
[[-20.  12.]
 [  1.   7.]
 [-17.  19.]
 [  8.   9.]
 [-14.  12.]
 [-17.  19.]
 [ -7.  15.]
 [  5.   1.]
 [-36.  25.]]
------------------------------------------
The final result is:flagishillissoeapy
meizhi@ubuntu:~/ctf$ python Hill.py -k '1,2;0,1' -p dloguszijluswogany
key is :
[[ 1.  0.]
 [-2.  1.]]
------------------------------------------
password matrix is:
[[ 4 12]
 [15  7]
 [21 19]
 [26  9]
 [10 12]
 [21 19]
 [23 15]
 [ 7  1]
 [14 25]]
------------------------------------------
The result matrix is:
[[-20.  12.]
 [  1.   7.]
 [-17.  19.]
 [  8.   9.]
 [-14.  12.]
 [-17.  19.]
 [ -7.  15.]
 [  5.   1.]
 [-36.  25.]]
------------------------------------------
The final result is:
flagishillissoeapy


'''