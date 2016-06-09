import conversions

class num_base:

    def __init__(self,value,base):
	value = str(value)	
	self.value = value
	self.base = base


    def convert(self,new_base,precision=5):
	number = conversions.todecimal(self.value,self.base)
	value = conversions.tobase(number,new_base,precision)
	self.value = value
	self.base = new_base
