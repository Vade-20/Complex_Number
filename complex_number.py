import re 
from fractions import Fraction
from math import sqrt

class Complex:
    def __init__(self,complex_number:str):
        self.__complex_number = complex_number
        self.__complex_number.replace('(','')
        self.__complex_number.replace(')','')
        assert self.iscomplex(),f'{self.complex_number} is not a proper complex number'
        real = re.findall(r'[-]?[\d\.//]+(?![i])\b',complex_number)
        imag = re.findall(r'([-]?[\d\.//]*)([i])',complex_number)
        real = list(map(lambda x:Complex.__useless(x),real))
        if len(real)>1:
            real = list(map(Fraction,real))
            real = [sum(real)]
        else:
            if real==[]:
                real = [Fraction(0)]
            else:
                real[0] = Fraction(real[0])
        if len(imag)>1:
            ans = 0
            for i in imag:
                if i[0]=='':
                    ans+=Fraction(1)
                elif i[0]=='-':
                    ans+=Fraction(-1)
                else:
                    ans+=Fraction(i[0])
            imag = [int(ans)]
        else:
            ans = imag[0][0] if imag !=[] else 0
            if ans=='':
                imag = [Fraction(1)]
            elif ans=='-':
                imag = [Fraction(-1)]
            else:
                imag = [Fraction(ans)]
            
        self.__real = real[0] if real!=[] else 0
        self.__imag = imag[0] if imag!=[] else 0
    
    def iscomplex(self):
        for i in self.__complex_number:
            if not i.isdigit() and i not in ['+','-','i','.','/']:
                return False
        else:
            return True
        
    @staticmethod 
    def __useless(x):
        if x[len(x)-1]=='/':
            return 0
        else:
            return x
    
    @property
    def complex_number(self):
        r = self.__real
        i = self.__imag
        if i>=0 and i.denominator==1:
            i = f'+{i}i'
        elif i<0 and i.denominator==1:
            i = f'{i}i'
        elif i>=0:
            i = f'+({i})i'
        else:
            i = f'-({-i})i'
        return f'{r}{i}'
    
    @property
    def real(self):
        return Fraction(self.__real) 
    
    @property
    def imag(self):
        i = self.__imag
        if i.denominator!=1:
            i = f'({i})i'
        else:
            i = f'{i}i'
        return i
    
    
    def __add__(self,second):
        real_new = self.__real+second.__real
        imag_new = second.__imag+self.__imag
        imag_new = f'+{imag_new}i' if imag_new>=0 else f'{imag_new}i'
        return Complex(f'{real_new}{imag_new}')
    
    def __sub__(self,second):
        real_new = self.__real-second.__real
        imag_new = self.__imag-second.__imag
        imag_new = f'+{imag_new}i' if imag_new>=0 else f'{imag_new}i'
        return Complex(f'{real_new}{imag_new}')
    
    def __mul__(self,second):
        x_1,y_1 = self.__real,self.__imag      
        x_2,y_2 = second.__real,second.__imag
        real_new = (x_1*x_2)-(y_1*y_2)
        imag_new = (x_1*y_2)+(x_2*y_1)
        imag_new = f'+{imag_new}' if imag_new>=0 else imag_new
        return Complex(f'{real_new}{imag_new}i')
    
    def __truediv__(self,second):
        x_1,y_1 = self.__real,self.__imag
        x_2,y_2 = second.__real,second.__imag
        real_new =Fraction(((x_1*x_2)+(y_1*y_2))/((x_2**2)+(y_2**2)))
        imag_new =-Fraction(((x_1*y_2)-(y_1*x_2))/((x_2**2)+(y_2**2)))
        imag_new = f'+{imag_new}i' if imag_new>=0 else f'{imag_new}i'
        return Complex(f'{real_new}{imag_new}')
        
    def congugate(self):
        real_new = self.__real
        imag_new = -self.__imag
        imag_new = f'+{imag_new}i' if imag_new>=0 else f'{imag_new}i'
        return Complex(f'{real_new}{imag_new}')
    
    def inverse(self):
        real_new = (self.__real)/((self.__real**2)+(self.__imag**2))
        imag_new = -(self.__imag)/((self.__real**2)+(self.__imag**2))
        imag_new =f'+{imag_new}i'if imag_new>=0 else f'{imag_new}i'
        return Complex(f'{real_new}{imag_new}')
    
    def modulous(self):
        return sqrt((self.__real**2)+(self.__imag**2))
    
    def sqrt_complex(self):
        a = self.__real
        b = self.__imag
        real_new = sqrt((self.modulous()+a)/2)
        imag_new = sqrt((self.modulous()-a)/2)
        if b<0:
            imag_new = -imag_new                 
        imag_new =f'+{imag_new}i'if imag_new>=0 else f'{imag_new}i'       
        return f'±({real_new}{imag_new})'
    
    def __str__(self) -> str:
        if self.iscomplex():
            return self.complex_number
        else:
            raise Exception ("Please enter a complex number")
        
