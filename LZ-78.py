#!/usr/bin/env python
#-*- coding:utf-8 -*-


class LZEncode:

	def __init__(self,inputText):

		self.inputText = inputText

		self.segment = []

		self.codeWord = []

		self.code = []

		self.length = 0

	def FillBin(self,bin):

		need = self.length - len(bin)

		if need != 0:

			bin = '0'*need + bin

		return bin 


	def CreateSegment(self):

		n = 0

		while 2**n < len(self.codeWord)+1:

			n = n + 1

		self.length = n

		self.segment = [self.FillBin(bin(i+1)[2:]) for i in range(len(self.codeWord))]

	def CreateWord(self):

		flag = ''

		for i in self.inputText:

			flag += i

			if self.codeWord.count(flag) == 0:

				self.codeWord.append(flag)

				flag = ''

	def ToGetCode(self,codeWord,num):

		if num == 1:

			return self.length*'0' + codeWord

		else:

			getIndex = self.codeWord.index(codeWord[0:-1])

			return self.segment[getIndex]+codeWord[-1]


	def Code(self):

		self.code = [self.ToGetCode(i,len(i)) for i in self.codeWord]


	def Encode(self):

		if ''.join(self.codeWord) != self.inputText:

			theLast = self.inputText[len(''.join(self.codeWord)):]

			getIndex = self.codeWord.index(theLast)

			return ''.join(self.code + [self.code[getIndex]]),len(self.codeWord),self.length

		else:

			return ''.join(self.code),len(self.codeWord)-1,self.length


	def Control(self):

		self.CreateWord()

		self.CreateSegment()

		self.Code()

		return self.Encode()


class LZDecode:

	def __init__(self,encodeText,length,codeLength):

		self.encodeText = encodeText

		self.length = length

		self.segment = []

		self.codeWord = []

		self.code = []

		self.length = length

		self.codeLength = codeLength

	def FillBin(self,bin,n):

		need = n - len(bin)

		if need != 0:

			bin = '0'*need + bin

		return bin 

	def CreateSegment(self):

		n = 0

		while 2**n < self.length+1:

			n = n + 1

		self.segment = [self.FillBin(bin(i+1)[2:],n) for i in range(self.length)]

	def CreateDict(self):

		self.CreateSegment()

		for i in range(len(self.encodeText)/(self.codeLength+1)):

			getOne = self.encodeText[i*(self.codeLength+1):(i+1)*(self.codeLength+1)]

			if getOne[0:self.codeLength] == '0'*self.codeLength:

				self.codeWord.append(getOne[self.codeLength])

			else:

				getSegmentIndex = self.segment.index(getOne[0:self.codeLength])

				self.codeWord.append(self.codeWord[getSegmentIndex]+getOne[self.codeLength])


		return ''.join(self.codeWord)







def main():

	#inputText = '00100101110110011'

	inputText = raw_input('Please input the bin you want you encode and decode:')

	lzEn = LZEncode(inputText)

	encode,length,codeLength = lzEn.Control()

	lzDe = LZDecode(encode,length,codeLength)

	decode = lzDe.CreateDict()

	print 'The source text is:' + inputText

	print 'The encode text is:' + encode

	print 'The decode text is:' + decode










if __name__ == '__main__':

	main()