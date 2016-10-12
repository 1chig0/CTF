import hashlib

ahash = '6ac66ed89ef9654cf25eb88c21f4ecd0'

citys = []

citys.append('thebronx')
citys.append('manhattan')
citys.append('newyork')
citys.append('richmond')
citys.append('queens')
citys.append('statenisland')
citys.append('brooklyn')


for first in range(0,1001):

	for city in citys:

		for last in range(10000,15001):

			string = 'ctf{' + str(first) + '_' + city + '_' + str(last) + '}'

			md5 = hashlib.md5()

			md5.update(string)

			n = md5.hexdigest()		

			if n == ahash:

				print md5.hexdigest

				print string

				print 'found'

