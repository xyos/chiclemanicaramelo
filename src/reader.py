'''
Created on Dec 23, 2009

@author: tuareg
'''
import sys
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.converter import XMLConverter,  TextConverter
from pdfminer.layout import LAParams

rsrc = PDFResourceManager()
filename="./19436849"
outfpxml = file(filename+".xml", 'w') #Si vamos a producir el xml, hagamos el archivo de salida un xml
outfptxt = file(filename+".txt", 'w')#Si vamos a producir el text, hagamos el archivo de salida un txt

laparams = LAParams()

devicexml = XMLConverter(rsrc, outfpxml, codec='utf-8', laparams=laparams) #Utilicemos el conversor a XML
devicetxt = TextConverter(rsrc, outfptxt, codec='utf-8', laparams=laparams) #Utilicemos el conversor a Texto

laparams.word_margin = 2.0
pagenos = set()
pagenos.add(0)

fp = file(filename+".pdf", 'rb')
process_pdf(rsrc, devicetxt, fp, pagenos, maxpages=0, password='')
process_pdf(rsrc, devicexml, fp, pagenos, maxpages=0, password='')
fp.close()
devicexml.close()
devicetxt.close()
outfpxml.close()
outfptxt.close()