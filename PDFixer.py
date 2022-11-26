import sys
import os
import shutil
import argparse
from tkinter import filedialog
import img2pdf
from pdf2image import convert_from_path
import pathlib
from fpdf import FPDF
###
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import Image

poppler_path = r"C:\Users\User\Documents\poppler-22.11.0\Library\bin"
###
class ImageFormats:
        JPG = "jpg"
        # PNG = "png"
        # TIFF = "tiff"
        # PPM = "ppm"
        
class Globals:
        temp_path = "C:\\pdfixer_files"
        middlepath = "C:\\pdfixer_files\\temp"
        extractedpath = "C:\\pdfixer_files\\extracted"
        input_file = ""
        output_dir = ""
        temporary_file = ""
        
####### TK #####

def create_temp_dir():
    os.makedirs(Globals.temp_path)
    tk.messagebox.showinfo(title=None, message="נוצרה תיקייה זמנית")
    print("temp created")

    



def browsefunc():
    filename = filedialog.askopenfilename(title='Please select a file')
    pathlabel1.config(text=filename)  
    Globals.input_file =  filename
    print(Globals.input_file)

    
def folderBrowse():
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    pathlabel2.config(text=dirname)
    Globals.output_dir = dirname
    print(Globals.output_dir)
    
def btnClickFunction():
    browsefunc()

def btnClickFunctionFolder():
    folderBrowse()

def move_pdf():
    temp_file = Globals.input_file
    shutil.copy(temp_file, Globals.temp_path)
    print("copied")
    Globals.temporary_file = temp_file
    print(Globals.temporary_file)
    tk.messagebox.showinfo(title=None, message="PDF moved")
    
    
    unpack_pdf()

def finish_operation():
    current = os.path.abspath(os.getcwd())
    shutil.copy(current+"\\"+"images.pdf", Globals.output_dir)
    tk.messagebox.showinfo(title=None, message="Done. Exit app")
    delete_temp_dir()
    root.quit()

def unpack_pdf():
    images = convert_from_path(Globals.temporary_file,  dpi=150, output_folder=Globals.middlepath, fmt='jpg')
    ###
    pdf = FPDF(orientation='P', format='A4')
    imgs = []

    img_list = [x for x in os.listdir(Globals.middlepath)]
        
    for img in img_list:
        pdf.add_page()
        imag = Globals.middlepath+"\\"+img
        pdf.image(imag, w=200, h=260)
    pdf.output("images.pdf")
    




root = Tk()
root.geometry('200x250')
root.resizable(0, 0)
root.configure(background='#A8BBBF')
root.title('Idan\'s PDFixer')
Button(root, text='1. Choose PDF file', bg='#F2E18D', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=25, y=50)
Button(root, text='2. Choose Output dir', bg='#F2EC9B', font=('arial', 12, 'normal'), command=btnClickFunctionFolder).place(x=25, y=100)  
Button(root, text='3. Render PDF file', bg='#F2EC9B', font=('arial', 12, 'normal'), command=move_pdf).place(x=25, y=150)
Button(root, text='4. Finish Operation', bg='#F2EC9B', font=('arial', 12, 'normal'), command=finish_operation).place(x=25, y=200)
pathlabel1 = Label(root)
pathlabel2 = Label(root)
pathlabel1.pack()
pathlabel2.pack()

#####
        
def create_temp_dir():
    os.makedirs(Globals.temp_path)
    print("temp created")
    os.makedirs(Globals.middlepath)
    print("middlepath created")
    os.makedirs(Globals.extractedpath)
    print("extractedpath created")
    # move_pdf()
    

def delete_temp_dir():
    shutil.rmtree(Globals.temp_path)
        


def main():
    tk.messagebox.showinfo(title="הוראות שימוש", message="יש לבצע את כל ארבעת השלבים לפי הסדר")
    create_temp_dir()
    root.mainloop()
    

    
if __name__ == "__main__":
    main()
    
    
    