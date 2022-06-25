import PyPDF2 as pdr

def combine_pdf(first_pdf, second_pdf, Combined_file):
    pdf1 = open(first_pdf, 'rb')
    pdf2 = open(second_pdf, 'rb')
    #create 2 pdf objects with data from pdf1 and pdf2
    obj1 = pdr.PdfFileReader(pdf1)
    obj2 = pdr.PdfFileReader(pdf2)
    #create a writer object
    writer = pdr.PdfFileWriter()
    #add pages from pdf1 and pdf2 to the writer object
    for i in range(obj1.numPages):
        page = obj1.getPage(i)
        writer.addPage(page)
    for i in range(obj2.numPages):
        page = obj2.getPage(i)
        writer.addPage(page)
    #create new pdf
    output_file = open(Combined_file, 'wb')
    #write to new pdf
    writer.write(output_file)
    pdf1.close()
    pdf2.close()
    output_file.close()
