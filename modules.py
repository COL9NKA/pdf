from pypdf import PdfMerger, PdfReader, PdfWriter
import os
import shutil


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
        
def Split_files (pdf, ranges):
    path = os.path.basename(pdf).replace(".pdf","")
    dir_path = "./files/"+path
    os.mkdir(dir_path)
    
    for rnge in ranges:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        range1 = int(rnge.split("-")[0])
        range2 = int(rnge.split("-")[1])
        page_range = range(range1, range2+1)

        for page_num, page in enumerate(reader.pages, 1):
            if page_num in page_range:
                writer.add_page(page)
        writer.close()

        writer.write("./files/"+path+"/"+path+"-"+str(range1)+"-"+str(range2)+".pdf")
    shutil.make_archive(dir_path, 'zip', dir_path)
    shutil.rmtree(dir_path)
    return (dir_path+".zip")

