digits = [chr(i) for i in range(48,58)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]

def tobase(number,base,precision=10):
    
    global digits

    base = int(base)

    n_int = abs(int(number))
    n_frac = abs(number-int(number))

    # Integer part
    h_int = ''
    while n_int!=0:
	r = n_int%base
	h_int = digits[r]+h_int
	n_int = n_int/base

    # Fractional part
    h_frac = ''
    for i in range(precision):
	n_frac = n_frac*base
	h_frac = h_frac+digits[int(n_frac)]
	n_frac = n_frac-int(n_frac)
    while ('errorfix'+h_frac)[-1]=='0':
	h_frac = h_frac[:-1]

    if number == 0:
	h_int = '0'
 
    if number < 0:
        h_int = '-'+h_int
 
    return h_int+'.'+h_frac
    
def todecimal(h,base):

    global digits
    
    if h[0]=='-':
        sign = -1.
        h = h[1:]
    else:
        sign = 1

    base = int(base)

    d = h.find('.')

    if d == -1:
	h_int = h
	h_frac = ''
    else:
	h_int=h[:d]
	h_frac=h[d+1:]

    n = 0
    for i in range(len(h_int)):
	n += digits.index(h_int[-1-i])*base**i
    for i in range(len(h_frac)):
	n += digits.index(h_frac[i])*base**(-1.-i)

    return sign*n