#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 09:11:41 2020

@author: daniel
"""

def sum(int1,int2):
    diff = abs(int1) > abs(int2)
    first = str(int1)
    second = str(int2)
    if (first[0] != '-' and (second[0] != '-')):
        return both_positive(first, second)
    elif (first[0] == '-' and (second[0] == '-')):
        return '-'+ both_positive(first[1:], second[1:])
    elif (first[0] == '-' and diff):
        return '-'+one_negative(first[1:],second)
    elif (second[0] == '-' and not diff):
        return '-'+one_negative(second[1:], first)
    elif (first[0] == '-' and not diff):
        return one_negative(second,first[1:])
    elif (second[0] == '-' and diff):
        return one_negative(first,second[1:])
    else: 
        return '0'
    
    
    
def both_positive(first,second):
    summ = ''    
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
def one_negative(first,second):
    summ = '' 
    second = '0'*(len(first)-len(second)) + second
    for i in range(len(first)):
        x = int(first[-i-1])
        y = int(second[-i-1])
        # print(x,y)
        if (x >=  y):            
            diff = str(x - y)   
            print(diff)
        elif (x <  y ):
            diff = str(x+10 - y)   
            # print(diff)
            # print(str(int(first[-i-2]) - 1))
            # print(first)
            x = first
            
            first = x[:-i-2] + str(int(x[-i-2]) - 1) + x[-i-1:]
            print(first)
            # print(first)
            
        summ = diff + summ
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
    # print(sum(-1234567890987654321323423541351451,-12345678987654321134143124123513551134))
    # print(multiply(152859965,912301))
    print(sum(1230, -123))
    
    