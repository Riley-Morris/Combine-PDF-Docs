import PyPDF2 as pdr


#list of pdfs to combine into one
pdfs_to_combine = []

def combine_pdf(pdf_list, Combined_file):
    #create a writer object
    writer = pdr.PdfFileWriter()
    #create new pdf with name/path from function input
    output_file = open(Combined_file, 'wb')
    for pdf_item in pdf_list:
        pdf1 = open(pdf_item, 'rb')
        #create  pdf object with data from pdf
        obj1 = pdr.PdfFileReader(pdf1)
        #add pages from pdf to the writer object
        for i in range(obj1.numPages):
            page = obj1.getPage(i)
            writer.addPage(page)
        #write to new pdf
        writer.write(output_file)
        pdf1.close()

    output_file.close()
