#!usr/bin/env python
#-*- coding:utf-8 -*-


from itertools import *

from optparse import *

def start():

	opt = OptionParser()

	opt.add_option('-c',dest='content',help='Input your content')

	opt.add_option('-o',dest='output',help='File to save the result')

	get,args = opt.parse_args()

	if get.content is None or get.output is None:

		print 'Use \'help\' to get help'

		exit(0)

	return get.content,get.output

def Exp(content,output):

	for i in range(2,len(content)):
		
		if len(content)%i == 0:

			filename = open(output,'a+')

			getList = Code(i)

			getCo = SplitStr(i,content)

			for num in getList:

				get = ''

				for s in getCo:

					for one in num:

						get = get + s[int(one):int(one)+1]

				filename.write(get+'\n')

			filename.close()

	print 'The result is saved as ' + output



def SplitStr(num,content):

	result = []

	for i in range(len(content)/num):

		result.append(content[i*num:(i+1)*num])

	return result



def Code(num):

	number = ''

	result = []

	for i in range(num):

		number = number + str(i)

	for i in permutations(number,num):

		result.append(i)

	return result


def main():

	content,output = start()

	Exp(content,output)



if __name__ == '__main__':

	main()