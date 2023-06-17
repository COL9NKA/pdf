import modules

'''
# --- Merge ---

print ("--- Merge ---")
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
'''


# --- Split ---

print ("--- Split ---")
print("Перенесите файл сюда и нажмите Enter: ", end = "")
pdf = input()
ranges = input("Введите диапазоны страниц через пробел (Пример: 1-2 4-5): ").split()

# файл появляется в папке files
result_path = modules.Split_files(pdf, ranges)

print ("файл создан: " + result_path)
input ()

# удаление файла
modules.Delete_file (result_path)

