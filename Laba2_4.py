f = []

try:
    f = open('file.txt','r')
    f.read()
except FileNotFoundError:
    print("файл не найден")
else:
    print("Файл найден")
finally:
    print("Спасибо за внимание")


