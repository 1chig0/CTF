#!/usr/bin/env python
# -*- coding:utf-8 -*-

def Deal(key,pw):

	pw = pw.lower()

	flag = 0

	lenght = len(key)

	while(len(key)<len(pw)):

		key = key + key[flag:flag+1]

		flag = flag + 1

		if flag == lenght:

			flag = 0

	if len(key)>len(pw):

		key =  key[0:len(pw)]

	return key,pw

def Exp(key,pw,code):

	result = ''

	yArr = []

	xArr = []

	for kword in key:

		for row in range(26):

			if code[row][0] == kword:

				yArr.append(row)


	for pword in pw:
		
		for col in range(26):

			if code[0][col] == pword:

				xArr.append(col)

	for num in range(len(pw)):

		result = result + code[yArr[num]][xArr[num]]

	print result

	print result.upper()



def Code():

	code = [[] for i in range(26)]

	for i in range(26):

		for j in range(26):

			num = 97 + i + j

			if num >= 123:

				num = num - 26

			code[i].append(chr(num))

	return code


def main():

	code = Code()

	key = raw_input("Input your key:")

	pw = raw_input("Input your password:")

	key,pw = Deal(key,pw)

	Exp(key,pw,code)


if __name__ == '__main__':

	main()