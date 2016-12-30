#!/usr/bin/env python
#-*- codingLutf-8 -*-


class LinerBlock:

	def __init__(self,codeLength,check,array,vectorM):

		self.codeLength = codeLength

		self.check = check

		self.array = array

		self.vectorM = vectorM

	def CreateArray(self,array):

		array = array.split(' ')

		step = len(array)/self.codeLength

		return [array[i*self.codeLength:(i+1)*self.codeLength] for i in range(step)]

	def Multiply(self,arrayM,arrayG):

		returnResutl = ''

		for i in range(len(arrayG[0])):

			colArray = [array[i] for array in arrayG]

			returnResutl += str(sum([int(x)*int(y) for x,y in zip(colArray,arrayM)])%2)

		return returnResutl

				



	def Encode(self):

		self.array = self.CreateArray(self.array)

		self.vectorM = self.vectorM.split()

		return self.Multiply(self.vectorM,self.array)




def main():

#	codeLength = 4

#	check = 3

#	array = '1 0 0 1 0 1 0 1 0 0 1 1'

#	vectorM = '1 0 1'

	codeLength = raw_input("Input length num:")

	check = raw_input("Input check num:")

	array = raw_input("Input array:")

	vectorM = raw_input("Input m:")

	linerBlock = LinerBlock(int(codeLength),int(check),array,vectorM)

	print 'The code is:' + linerBlock.Encode()




if __name__ == '__main__':

	main()