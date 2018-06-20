# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:24:00 2018

@author: AAKASH
"""

class Parent:
    def __init__(Self,name,id):
        Self.name=name;
        Self.id=id;
        
    def display(Self):
        print(Self.name)
       
class Base(Parent):
    def __init__(Self,name):
        Self.name=name
        
base=Base("Aakash")
base.display()        