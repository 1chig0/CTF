#!usr/bin/env python
# -*- coding:utf-8 -*-

from optparse import OptionParser


def Start():

	start = OptionParser()

	start.add_option('-p',dest='pw',help='Passwd')

	start.add_option('-a',dest='getA',help='\'A\' word')

	start.add_option('-b',dest='getB',help='\'B\' word')

	options,args = start.parse_args()

	if options.pw is None or options.getA is None or options.getB is None:

		print 'Please input \'-h\' to get help'

		exit(0)

	return options

def Deal(options):

	pw = options.pw.lower()

	getA = options.getA

	getB = options.getB

	if len(pw)%5 != 0:

		print 'Illegal passwd'

		exit(0)

	result = ''

	for i in range(len(pw)/5):

		string = pw[i*5:(i+1)*5]

		string = string.replace(getA,'0')

		string = string.replace(getB,'1')

		result = result + chr(int(string,2)+97)

	print result



def main():

	options = Start()

	Deal(options)


if __name__ == '__main__':

	main()