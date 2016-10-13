#!usr/bin/env python
#-*- coding:utf-8 -*-
'''

Usage: KeyBoardPw.py -c (your content)


'''
from optparse import OptionParser


def ArgsModule():

	Arg = OptionParser()

	Arg.add_option('-c',dest='content',help='Input your content')

	options,args = Arg.parse_args()

	if options.content is None:

		print 'Please input \'-h\' to get help'

		exit(0)

	return options.content


def Code():

	code = {

			'a':'q','b':'w','c':'e','d':'r',
			'e':'t','f':'y','g':'u','h':'i',
			'i':'o','j':'p','k':'a','l':'s',
			'm':'d','n':'f','o':'g','p':'h',
			'q':'j','r':'k','s':'l','t':'z',
			'u':'x','v':'c','w':'v','x':'b',
			'y':'n','z':'m'
	}

	return code

def exp(content):

	code = Code()

	result = ''

	for i in content:

		for key,value in code.items():

			if value == i:

				result = result + key

	print result

	

def main():

	content = ArgsModule()
	
	exp(content)



if __name__ == '__main__':

	main()