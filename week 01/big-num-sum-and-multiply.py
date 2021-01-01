#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 09:11:41 2020

@author: daniel
"""

def sum(int1,int2):
    first = str(int1)
    second = str(int2)
    summ = ''    
    sign = '-' (if first[0] == '-' or second[0] == '-' ) and 
    carry = 0
    a = len(first)
    b = len(second)
    c = abs(a-b)
    if(a<b):
        first = '0'*c + first
    else:
        second = '0'* c + second
    
    for i in range(a if a >= b else b):
        d = str(int(first[-i-1])+int(second[-i-1])+int(carry))
        if len(d) > 1:
            summ = d[1] + summ
            carry = d[0]
        else:
            summ = d[0] + summ
            carry = '0'
    summ = carry + summ   
    summ = summ[1:] if summ[0] == '0' else summ   
    return summ

def multiply(int1,int2):
    first = str(int1)
    second = str(int2)
    final = ''
    carry = 0
    for i in range(len(second)):
        mult = ''
        for j in range(len(first)):
            
            m = str(int(first[-j-1]) * int(second[-i-1]) + int(carry))
            if len(m) >1:
                mult = m[-1] +mult
                carry = m[0:-1]
            else:   
                mult = m[0] + mult
                carry = '0'
        mult = carry + mult + '0'* (i)
        mult = mult[1:] if mult[0] == '0' else mult  
        final =  sum(final , mult)
    return final
            
             
if __name__ == "__main__":
    # print(sum(1234567890987654321323423541351451,12345678987654321134143124123513551134))
    # print(multiply(152859965,912301))
    
    