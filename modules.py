from pypdf import PdfMerger


n = int(input("Введите количество pdf файлов: "))
pdfs = []
for i in range(n):
    print("Перенесите файл сюда и нажмите Enter: ", end = "")
    pdfs.append(input())
    
#pdfs = ['C:\\Users\\ponomarev\\Desktop\\uiop\\dev\\1.pdf', 'C:\\Users\\ponomarev\\Desktop\\uiop\\dev\\2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

path = pdfs[0]
path = '\\'.join(path.split('\\')[:-1])


end_path = path + "\\res.pdf"
print(end_path)
merger.write(end_path)
merger.close()