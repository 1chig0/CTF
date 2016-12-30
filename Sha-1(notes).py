#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Sha1类接收inputText参数(明文)
'''
class Sha1:

	#接收方法
	def __init__(self,inputText):

		self.inputText = inputText

		self.WtList = []

	#扩充字符串到固定位数(不够就补0)
	def FillBin(self,bin,num):

		need = num - len(bin)

		if need != 0:

			bin = '0'*need + bin

		return bin

	#初始话字符串的时候需要扩充到512位
	def FillInitialBin(self,firstText):

		need = 448 - len(firstText)

		if need >= 1:

			firstText = firstText + '1' + (need-1)*'0' + self.FillBin(bin(len(self.inputText)*8)[2:],64)

		return firstText
	
	#调用字符串扩充方法,将处理后得到的结果返回
	def InitialText(self):

		return self.FillInitialBin(''.join([self.FillBin(bin(int(ord(i)))[2:],8) for i in self.inputText]))

	#返回Kt常量
	def ReturnKt(self):

		return ['5a827999','6ed9eba1','8f1bbcdc','ca62c1d6']

	#初始化寄存器
	def InitialRegister(self):

		return ['67452301','efcdab89','98badcfe','10325476','c3d2e1f0']

	#十六进制转二进制
	def HexToBin(self,hexString):

		return ''.join([self.FillBin(bin(int(i,16))[2:],4) for i in hexString])
	
	#二进制转十六进制
	def BinToHex(self,binString):

		return ''.join([hex(int(binString[4*i:4*(i+1)],2))[2:] for i in range(len(binString)/4)])

	#讲bin字符串左移num个位数
	def LeftMove(self,bin,num):

		for i in range(num):

			bin = bin[1:] + bin[0]

		return bin

	#F函数操作
	def OperatorF(self,BCD,t):

		BCD = int((BCD),2)

		f = [[0,1,0,1,0,0,1,1],[0,1,1,0,1,0,0,1],[0,0,0,1,0,1,1,1],[0,1,1,0,1,0,0,1]]

		return str(f[t/20][BCD])

	#对number取余数
	def GetMod(self,number,mod):

		return number%mod

	#对这一轮的E寄存器操作并将结果返回个A寄存器
	def EToA(self,f,E,LeftMoveA,w,k):

		first = self.GetMod(int(f,2)+int(E,2),2**32)

		second = self.GetMod(first+int(LeftMoveA,2),2**32)

		third = self.GetMod(second+int(w,2),2**32)

		forth = self.GetMod(third+int(k,2),2**32)

		return self.FillBin(bin(forth)[2:],32)

	#根据轮数返回Wt
	def Wt(self,num):

		allInitialText = self.InitialText()

		if num <= 15:

			return allInitialText[num*32:(num+1)*32]

		else:

			number = ''.join([str(int(a)^int(b)^int(c)^int(d)) for a,b,c,d in zip(self.WtList[num-16],self.WtList[num-14],self.WtList[num-8],self.WtList[num-3])])
			
			return self.LeftMove(number,1)

	#根据轮数返回Kt
	def Kt(self,num):

		return self.HexToBin(self.ReturnKt()[num/20])

	#加密控制器
	def Control(self):

		getInitialRegister = [self.HexToBin(i) for i in self.InitialRegister()]

		A,B,C,D,E = getInitialRegister[0],getInitialRegister[1],getInitialRegister[2],getInitialRegister[3],getInitialRegister[4]
		
		initalA,initalB,initalC,initalD,initalE = A,B,C,D,E

		for num in range(80):

			print '-'*50

			w = self.Wt(num)

			print num

			self.WtList.append(w)

			k = self.Kt(num)

			f = ''.join([self.OperatorF(b+c+d,num) for b,c,d in zip(list(B),list(C),list(D))])

			A,B,C,D,E = self.EToA(f,E,self.LeftMove(A,5),w,k),A,self.LeftMove(B,30),C,D

			print 'A:' + self.BinToHex(A)

			print 'B:' + self.BinToHex(B)

			print 'C:' + self.BinToHex(C)

			print 'D:' + self.BinToHex(D)

			print 'E:' + self.BinToHex(E)


		
		A = self.BinToHex(self.FillBin(bin(self.GetMod(int(A,2)+int(initalA,2),2**32))[2:],32))

		B = self.BinToHex(self.FillBin(bin(self.GetMod(int(B,2)+int(initalB,2),2**32))[2:],32))

		C = self.BinToHex(self.FillBin(bin(self.GetMod(int(C,2)+int(initalC,2),2**32))[2:],32))

		D = self.BinToHex(self.FillBin(bin(self.GetMod(int(D,2)+int(initalD,2),2**32))[2:],32))

		E = self.BinToHex(self.FillBin(bin(self.GetMod(int(E,2)+int(initalE,2),2**32))[2:],32))


		print '-'*50

		print 'The secrect text is:' + A+B+C+D+E


def main():


	sha1 = Sha1('abc')

	sha1.Control()


if __name__ == '__main__':

	main()
