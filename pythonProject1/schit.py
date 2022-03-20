import re
import webbrowser
import time
# получим объект файла
file1 = open("ee.txt", "r")
# считываем все строки
lines = file1.readlines()
# итерация по строкам
arr = []
for line in lines:
    if "https://vulners.com/" in line:
        arr.append(line)
        print(line)

for a in arr:
    tmp = a.split()
    tmp_name = tmp[1]
    tmp_risk = tmp[2]
    tmp_href = tmp[3]
    # открываем ссылки в вулнерс, каждые 10 сек следующую
   # webbrowser.open(tmp_href)
   # time.sleep(10)

    print(tmp[1])
    #print(tmp[2])
    print(tmp[3])
    # закрываем файл
file1.close