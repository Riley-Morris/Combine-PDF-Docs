import PyPDF2 as pdr
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk

import os


txt_font = ('Cambria', 20)
butt_font = ('Lucida Sans Unicode', 12)
class BigWindow:

    pdf_list = []
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        #set style
        style = ttk.Style(self.root)
        style.theme_use('alt')
        #button that adds pdfs
        OpenButton = Button(self.root, text = 'Click to add a PDF', command = self.add_pdf, font = butt_font, relief = 'raised', borderwidth = 3).grid(column =0, row = 0, sticky = 'W', padx = 5, columnspan = 2)
        #button to combine pdfs
        Combine_Button = Button(self.root, text = 'Combine PDFs', font = butt_font, command = lambda: self.save_file(), relief = 'raised', borderwidth = 3).grid(column = 0, row = 9, sticky = 'W', padx = 5, columnspan = 2)
        #labels for pdf files
        Label1 = Label(self.root, text = 'File 1:', font = txt_font).grid(column = 0, row =1, sticky = 'W', padx = 5)
        Label2 = Label(self.root, text='File 2:', font = txt_font).grid(column=0, row=2, sticky = 'W', padx = 5)
        Label3 = Label(self.root, text='File 3:', font = txt_font).grid(column=0, row=3, sticky = 'W', padx = 5)
        Label4 = Label(self.root, text='File 4:', font = txt_font).grid(column=0, row=4, sticky = 'W', padx = 5)
        Label5 = Label(self.root, text='File 5:', font = txt_font).grid(column=0, row=5, sticky = 'W', padx = 5)
        Label6 = Label(self.root, text='File 6:', font = txt_font).grid(column=0, row=6, sticky = 'W', padx = 5)
        Label7 = Label(self.root, text='File 7:', font = txt_font).grid(column=0, row=7, sticky = 'W', padx = 5)
        Label8 = Label(self.root, text='File 8:', font = txt_font).grid(column=0, row=8, sticky = 'W', padx = 5)

        self.root.mainloop()

        #function that adds and displays pdfs to combine
    def add_pdf(self):
        self.root.filename = filedialog.askopenfilename(title="Select Pdf files to combine",
                                                        filetypes=[("Pdf files", "*.pdf")])
        self.pdf_list.append(self.root.filename)
        clicked_label = Label(self.root, text= self.root.filename, font = txt_font).grid(column =1, row = len(self.pdf_list), sticky = 'W')

        #function that combines pdf and outputs a file
    def save_file(self):
        f = asksaveasfile(initialfile = 'Untitled.pdf', defaultextension="*.*", filetype=[('PDF Document', '*.pdf')])
        #call for combine function with name (path) of save file chosen in dialog
        self.combine_pdf(f.name)
        #create new window to with button to close app
        closewindow = Toplevel(self.root)
        closewindow.title('Pdf Combiner')
        closewindow.geometry('240x58')
        close_frame = Frame(closewindow)
        close_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        closebutton = Button(close_frame, text = 'File has been created!\nClick to close', command=self.root.destroy, relief = 'raised', font = butt_font, borderwidth = 3).grid(row=0, column=0)

    def combine_pdf(self, Combined_file):
        # create a writer object
        writer = pdr.PdfFileWriter()
        # create new pdf with name/path from function input
        output_file = open(Combined_file, 'wb')
        for pdf_item in self.pdf_list:
            pdf1 = open(pdf_item, 'rb')
            # create  pdf object with data from pdf
            obj1 = pdr.PdfFileReader(pdf1)
            # add pages from pdf to the writer object
            for i in range(obj1.numPages):
                page = obj1.getPage(i)
                writer.addPage(page)
            # write to new pdf
            writer.write(output_file)
            pdf1.close()

        output_file.close()

class Main:
    root = Tk()
    Window1 = BigWindow(root, "PDF Combiner", "600x380")

Main()
