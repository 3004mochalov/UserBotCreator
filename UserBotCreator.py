import os
from tkinter import *
import tkinter as tk
import pyautogui
import winsound
import tkinter.messagebox as mb
import datetime
from threading import Thread


f = open('Ccord.txt', 'w') #сброс содержимого в файле
f.flush()
f.write('=YEAR=MONTH=DAY=HH:MM:SS=STATUS==========\n')
f.close()


class Test():
   def __init__(self):
        self.root = tk.Tk() #выбор языка для работы
        self.root.title("Choose the Language:")
        self.root.geometry('300x25')
        self.root.iconphoto(True, tk.PhotoImage(file='icon.png'))
        btn = Button(self.root, text='Русский', command=self.rus)
        btn.grid(column=0, row=0)
        btn = Button(self.root, text='English', command=self.eng)
        btn.grid(column=1, row=0)
        self.root.mainloop()

   def WriteLocation(self):

       n = 0 #таймер с предупреждающими звуковыми сигналами
       while n != 1:
           winsound.Beep(300, 1000)
           n += 1
       n = 0
       while n != 4:
           winsound.Beep(300, 500)
           n += 1
       n = 0
       while n != 4:
           winsound.Beep(300, 300)
           n += 1
       n = 0
       while n != 3:
           winsound.Beep(400, 200)
           n += 1

       currentMouseX, currentMouseY = pyautogui.position() #присваивание значений для последующей записи файл
       x = currentMouseX
       y = currentMouseY

       with open('Ccord.txt') as file_in:
           text = file_in.read()
       text = text.replace(" resent", "")
       with open("Ccord.txt", "w") as file_out:
           file_out.write(text)

       f = open('Ccord.txt', 'a') #процесс записи полученных значений в файл
       f.write(str(datetime.datetime.now()) + ' resent:\n')
       f.write('x = ' + str(x) + '\n')
       f.write('y = ' + str(y) + '\n')
       f.write('=========================================\n')
       f.close()

       def show_info():
           answer = mb.askyesno(title="Информация", message="Координаты записаны, открыть файл?") #вывод информации
           if answer:
               self.OpenTxt()

       show_info()
   def NewFile(self):
       pass

   def SaveFile(self):
       pass

   def OpenFile(self):
       pass

   def OpenTxt(self):
       os.startfile(r'"Ccord.txt"') #открытие файла в окне

   def CursorMenu(self):
       self.root = tk.Tk() #Меню курсора
       self.root.title("Меню Курсора")
       self.root.geometry('300x200')
       btn = Button(self.root, text='записать координаты', command=self.WriteLocation)
       btn.place(x=100, y=170)
       btn = Button(self.root, text='Отчёт о координатах', command=self.OpenTxt)
       btn.place(x=100, y=80)
       self.root.mainloop()

   def CursorMenuConfigure(self):
       thread1 = Thread(target=self.CursorMenu()) #изначально хотел чтоб программа после записи значений
#                                                  записывал в текстовое окно, но из-за ошибки программы и сложности его решения
       thread1.start() #                           было принято, что программа будет записывать полученные координаты курсора в текстовый файл
       thread1.join()

   def MainEnglish(self):
       window = Tk() #основное окно будущего редактора на английском языке (полностью не готов)
       window.title("UserBotCreator")
       window.geometry('1280x600')
       menu = Menu(window)
       new_item = Menu(menu, tearoff=0)
       new_item2 = Menu(menu, tearoff=0)
       new_item2.add_command(label='Cursor menu', command=self.CursorMenuConfigure)
       new_item.add_command(label='Create', command=self.NewFile)
       new_item.add_command(label='Save', command=self.SaveFile)
       new_item.add_command(label='Open', command=self.OpenFile)
       menu.add_cascade(label='File', menu=new_item)
       menu.add_cascade(label='Tools', menu=new_item2)
       window.config(menu=menu)
       window.mainloop()

   def MainRussian(self):
       window = Tk() #основное окно будущего редактора на русском языке
       window.title("UserBotCreator")
       window.geometry('1280x600')

       menu = Menu(window)
       new_item = Menu(menu, tearoff=0)
       new_item2 = Menu(menu, tearoff=0)
       new_item2.add_command(label='Меню Курсора', command=self.CursorMenuConfigure)
       new_item.add_command(label='Создать', command=self.NewFile)
       new_item.add_command(label='Сохранить', command=self.SaveFile)
       new_item.add_command(label='Открыть', command=self.OpenFile)
       menu.add_cascade(label='Файл', menu=new_item)
       menu.add_cascade(label='Инструменты', menu=new_item2)

#       self.img = tk.PhotoImage(file="CursorButton.png")
#       self.btn = Button(self.root, image=self.img, compound=tk.LEFT, command=self.OpenTxt)
#       self.btn.place(x=100, y=80)

       window.config(menu=menu)
       window.mainloop()

   def rus(self):
       self.MainRussian()
       self.root.destroy() #функция открытия русской вариации программы


   def eng(self):
       self.MainEnglish()
       self.root.destroy() #функция открытия английской вариации программы





app = Test()

