#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

def start():

	n = 2

	result = []

	while (n<920139713):
	    

		if (920139713%n == 0):
	    
			result.append([n,920139713/n])

		n = n + 1

	return result


def egcd(a,b):

	if a == 0:

		return 0,1

	else:

		y,x = egcd(b%a,a)

		return x-(b//a)*y,y


def main():

#	result = start()

	result = [[18443,49891]]

	for i in result:

		fi = (i[0]-1)*(i[1]-1)

		s = egcd(19,fi)

	if s[0]>0:

		key = s[0]

	else:

		key = s[1]

#	get = 704796792

	words = ''

	filename = open('1.txt','r')

	for get in filename.readlines():

		word = pow(int(get),key,920139713)

		words = words + chr(int(word))

	print words






if __name__ == '__main__':

	main()



'''
1.txt


704796792
752211152
274704164
18414022
368270835
483295235
263072905
459788476
483295235
459788476
663551792
475206804
459788476
428313374
475206804
459788476
425392137
704796792
458265677
341524652
483295235
534149509
425392137
428313374
425392137
341524652
458265677
263072905
483295235
828509797
341524652
425392137
475206804
428313374
483295235
475206804
459788476
306220148


'''