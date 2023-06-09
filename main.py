import modules

# --- Merge ---
n = int(input("Введите количество pdf файлов: "))
pdfs = []
for i in range(n):
    print("Перенесите файл сюда и нажмите Enter: ", end = "")
    pdfs.append(input())

# файл появляется в папке files
result_path = modules.Merge_files(pdfs)

print ("файл создан: " + result_path)
input ()

# удаление файла
modules.Delete_file (result_path)


