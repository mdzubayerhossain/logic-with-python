from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    #this take a pdf start page & end page & file name
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf = PdfFileWriter()

    ostream = open(file.split(".")[0] + "cropped"+".pdf","wb")

    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))

        outPdf.write(ostream)
        
        start += 1
    ostream.close()


if __name__ == "__main__":
    cropper(1,5,"sample.pdf")