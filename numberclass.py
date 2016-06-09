from __future__ import division
from conversions import *

class num_base:

    def __init__(self,value,base):
	value = str(value)	
	self.value = value
	self.base = base


    def convert(self,new_base,precision=20):
	number = todecimal(self.value,self.base)
	value = tobase(number,new_base,precision)
	self.value = value
	self.base = new_base

    def __add__(self,other):
        res = todecimal(self.value,self.base)+todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)

    def __sub__(self,other):
        res = todecimal(self.value,self.base)-todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)

    def __mul__(self,other):
        res = todecimal(self.value,self.base)*todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)

    def __div__(self,other):
        res = todecimal(self.value,self.base)/todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)

    def __floordiv__(self,other):
        res = todecimal(self.value,self.base)//todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)
        
    def __truediv__(self,other):
        res = todecimal(self.value,self.base).__truediv__(todecimal(other.value,other.base))
        return num_base(tobase(res,self.base),self.base)

    def __pow__(self,other):
        res = todecimal(self.value,self.base)**todecimal(other.value,other.base)
        return num_base(tobase(res,self.base),self.base)

    def __abs__(self):
        if self.value[0] == '-':
            self.value = self.value[1:]

    def __eq__(self,other):
        return todecimal(self.value,self.base).__eq__(todecimal(other.value,other.base))

    def __ne__(self,other):
        return todecimal(self.value,self.base).__ne__(todecimal(other.value,other.base))

    def __ge__(self,other):
        return todecimal(self.value,self.base).__ge__(todecimal(other.value,other.base))

    def __gt__(self,other):
        return todecimal(self.value,self.base).__gt__(todecimal(other.value,other.base))

    def __le__(self,other):
        return todecimal(self.value,self.base).__le__(todecimal(other.value,other.base))

    def __lt__(self,other):
        return todecimal(self.value,self.base).__lt__(todecimal(other.value,other.base))