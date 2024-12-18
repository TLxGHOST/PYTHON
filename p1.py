import PyPDF2 as pd
print("Hello world")
print("How are you?")
print("this program will merge two pdf files")
s=input("Enter the name of the first pdf file: ")
s1=input("Enter the name of the second pdf file: ")
#opening the pdf files
p1 = open(s,'rb')
p2 = open(s1,'rb')
#creating a pdf reader object
pdf1 = pd.PdfFileReader(p1)
pdf2 = pd.PdfFileReader(p2)
#creating a pdf writer object
pdfWriter = pd.PdfFileWriter()
#adding the pages of pdf1 to pdfWriter object
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
#adding the pages of pdf2 to pdfWriter object
for pageNum in range(pdf2.numPages):
    pageObj = pdf2.getPage(pageNum)
    pdfWriter.addPage(pageObj)
#opening the final pdf file in write binary mode
pdfOutputFile = open('merged.pdf','wb')
#writing the pdf file
pdfWriter.write(pdfOutputFile)
#closing the pdf file object
pdfOutputFile.close()
p1.close()
p2.close()
print("Merging of pdf files is completed")
