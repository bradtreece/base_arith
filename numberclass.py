from conversions import *

class num_base:

    def __init__(self,value,base):
	value = str(value)	
	self.value = value
	self.base = base


    def convert(self,new_base,precision=10):
	number = todecimal(self.value,self.base)
	value = tobase(number,new_base,precision)
	self.value = value
	self.base = new_base

    def __add__(self,other):
        res = todecimal(self.value,self.base)+todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)