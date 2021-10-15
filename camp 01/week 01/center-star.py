#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:24:59 2021

@author: daniel
"""

def centerodd(n):
    x =n -1
    for i in range(n):
        print(' '*x+'*'*(2*i-1))
        x -= 1


if __name__ == "__main__":
    centerodd(6)