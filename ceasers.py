''' Simple encryption and decryption algorithm'''
class Ceasers(object):
	
	def __init__(self,shift):
		encode =[None]*26
		decode =[None]*26
		for k in range(26):
			encode[k] = chr((k+shift) % 26 +ord('A'))
			decode[k] = chr((k-shift) % 26 +ord('A'))
		self._forward = ''.join(encode)
		self._backward = ''.join(decode)

	def encrtpy(self,message):
		return self._transform(message,self._forward)

	def decrypt(self,code):
		return self._transform(code,self._backward)

	def _transform(self,original,code):
		msg = list(original)
		for k in xrange(len(msg)):
			if msg[k].isupper():
				j = (ord(msg[k]) - ord('A'))
				msg[k]  = code[j]
		return ''.join(msg)

if __name__ == '__main__':
	cipher = Ceasers(3)
	message = "THE EAGLE HAS LANDED"
	code = cipher.encrtpy(message)
	print code
	print cipher.decrypt(code)
	print cipher._forward
	print cipher._backward