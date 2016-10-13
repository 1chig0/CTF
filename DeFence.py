#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
1.Usage: DeFence.py -c content

2.Usage: DeFence.py -c content -n (A number)

'''

from optparse import OptionParser


def ArgsModule():

	Arg =  OptionParser()

	Arg.add_option('-c',dest='content',help='Input the passwd')

	Arg.add_option('-n',dest='num',help='Number of Fence,deault is half of content')

	options,args = Arg.parse_args()

	if options.content is None:

		print 'Please input \'-h\' to get help'

		exit(0)

	return options


def exp(content,num,quote):

	result = []

	key = ''

	for i in range(quote):

		result.append(content[i*num:(i+1)*num])

	for n in range(num):

		for string in result:

			key = key + string[n:n+1]

	print key


		



def DealArgs(options):

	if options.num is not None:

		quote = len(options.content)/int(options.num)

		exp(options.content,int(options.num),quote)

	else:

		num = len(options.content)/2

		for i in range(2,num+1):

			if len(options.content)%i == 0:

				quote = len(options.content)/i

				exp(options.content,i,quote)


def main():

	options = ArgsModule()

	DealArgs(options)


if __name__ == '__main__':

	main()