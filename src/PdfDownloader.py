# -*- coding: utf-8 -*-
"""
Esta clase crea un objeto de tipo Thread, que recibe como parametros un valor inicial
y uno final, itera en esos valores descargando los pdfs que genere la aplicación de telmex
, se debe instanciar de la siguiente forma:
objetox = PdfDownloader(valor1,valor2).start()
donde valor1 y valor 2 son enteros positivos.
"""
import httplib
import threading

HOST="190.27.201.2"
URL="/bill_telmex.php?JULIO="
DIR="./facturas"

class PdfDownloader(threading.Thread):
	def __init__(self,ini,fin):
		self.ini= ini
		self.fin= fin
		threading.Thread.__init__(self)
	def run(self):
		self.download(self.ini,self.fin)
	def savepdf(self,num,pdffile):
		filename = DIR+str(num)+".pdf"
		fileout = file(filename,'w')
		fileout.write(pdffile)
		fileout.close
	def download(self,ini,fin):
		for num in xrange(ini,fin):
			conection = httplib.HTTPConnection(HOST)
			conection.request("GET", URL + str(num))
			response = conection.getresponse()
			if response.getheader('content-type') == 'application/pdf':
				print num
				pdffile = response.read()
				self.savepdf(num,pdffile)
			conection.close

