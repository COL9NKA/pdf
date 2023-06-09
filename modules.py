from pypdf import PdfMerger
import os

def Merge_files (list_pdfs):
    merger = PdfMerger()

    for pdf in list_pdfs:
        merger.append(pdf)

    path = os.path.basename(list_pdfs[0]).replace(".pdf","")

    merger.write("./files/"+path+"_merged.pdf")
    merger.close()
    
    return ("./files/"+path+"_merged.pdf")
    
def Delete_file (list_path):
    os.remove(list_path)
        
def Delete_many_files (list_path):
    for path in list_path:
        os.remove(path)