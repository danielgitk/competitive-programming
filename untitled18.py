#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:04:49 2021

@author: daniel
"""
size = 0
items = []


    
def getLeft(ind): return 2*ind + 1
def getRight(ind): return 2*ind + 2
def getParent(ind): return (ind -1) // 2

def hasLeft(ind): return getLeft(ind) < size
def hasRight(ind): return getRight(ind) < size
def hasParent(ind): return getParent(ind) >= 0

def leftChild(ind): return items[getLeft(ind)]
def rightChild(ind): return items[getRight(ind)]
def parent(ind): return items[getParent(ind)]
    
def swap(left, right):items[left],items[right] = items[right], items[left]

