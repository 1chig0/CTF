#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


class Rsa:

	def __init__(self,p,q,e,inputText):

		self.e = e

		self.p = p

		self.q = q

		self.fi = (self.p-1)*(self.q-1)

		self.n = self.p*self.q

		self.inputText = inputText

	def Gcd(self,fi,e):

		if e == 0:

			return 0,1

		else:

			y,x = self.Gcd(e,fi%e)

			return x-(fi//e)*y,y

	def FastExpMod(self,baseNumber, e, mod):

		result = 1

		while e != 0:

			if (e&1) == 1:

				result = (result * baseNumber) % mod
			
			e >>= 1

			baseNumber = (baseNumber*baseNumber) % mod
			
		return result

	def PrivateKey(self):

		s = self.Gcd(self.fi,self.e)

		if s[0] > 0:

			key = s[0]

		else:

			key = s[1]

		return key

	def DealNumber(self,num,need):

		if need - len(num) != 0:

			num = '0'*(need-len(num)) + num

		return num

	def DealText(self,text):

		return ''.join([self.DealNumber(str(ord(i)-97),2) for i in text])

	def CreateRandomNumber(self,start,end):

		return random.randint(start,end)


	def Encode(self):

		getInputText = self.DealText(self.inputText)

		return ''.join([self.DealNumber(str(self.FastExpMod(int(getInputText[i*4:(i+1)*4]),self.e,self.n)),4) for i in range(len(getInputText)/4)])

	def Decode(self,encryptText):

		privateKey = self.PrivateKey()

		getText = ''.join([self.DealNumber(str(self.FastExpMod(int(encryptText[i*4:(i+1)*4]),privateKey,self.n)),4) for i in range(len(encryptText)/4)])
	
		return ''.join([chr(97 + int(getText[i*2:(i+1)*2])) for i in range(len(getText)/2)])


def main():

	p=43
	
	q=59

	e=13
	
	#if wanted to get the random num for p,q,e,you call use the function I have written in the class rsa
	#its name is CreateRandomNumber()


	text = 'public'

	rsa = Rsa(43,59,13,text)

	print "Text:" + text

	encryptText = rsa.Encode()

	print "Encrypt:" + encryptText

	decryptText = rsa.Decode(encryptText)

	print "Decrypt:" + decryptText



if __name__ == '__main__':

	main()