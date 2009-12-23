'''
Created on Dec 23, 2009

@author: tuareg
'''
from xml.dom.minidom import parse
midom=parse("./facturas/42739003.xml")
print midom.