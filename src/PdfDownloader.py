# -*- coding: utf-8 -*-
"""
Esta clase crea un objeto de tipo Thread, que recibe como parametros un valor inicial
y uno final, itera en esos valores descargando los pdfs que genere la aplicación de telmex, 
en el proceso los convierte a xml, se debe instanciar de la siguiente forma:
objetox = PdfDownloader(valor1,valor2).start()
donde valor1 y valor 2 son enteros positivos.
"""
import httplib
import threading
from pdfminer.converter import XMLConverter
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

HOST="xxx.xxx.xxx.xxx"
URL="/bill_telmex.php?JULIO="
DIR="./facturas/"


class PdfDownloader(threading.Thread):


	def __init__(self,ini,fin):
		self.ini= ini
		self.fin= fin
		threading.Thread.__init__(self)


	def run(self):
		self.download(self.ini,self.fin)


	def savepdf(self,filename,pdffile):
		fileout = file(filename+".pdf",'w')
		fileout.write(pdffile)
		fileout.close
	
	def to_xml(self, filename):
		src = file(filename+".pdf",'rb')
		out = file(filename+".xml", 'w')
		rsrc = PDFResourceManager()
		converter = XMLConverter(rsrc, out, codec='utf-8', laparams=None)
		process_pdf(rsrc, converter, src, 0, maxpages=0, password='')
		src.close
		out.close
		converter.close
		
	def download(self,ini,fin):
		for num in xrange(ini,fin):
			conection = httplib.HTTPConnection(HOST)
			conection.request("GET", URL + str(num))
			response = conection.getresponse()
			if response.getheader('content-type') == 'application/pdf':
				print num
				pdffile = response.read()
				filename = DIR+str(num)
				self.savepdf(filename,pdffile)
				self.to_xml(filename)
			conection.close
