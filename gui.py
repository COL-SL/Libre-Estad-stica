#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Copyright (C) 2017  Manuel David Jim�nez Pati�o

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
'''

import pygtk
pygtk.require('2.0')
import gtk
from shutil import copyfile
import pandas as pd
import numpy as np
import Tkinter as tk
from Tkinter import *
from scipy import stats
import statistics as st
from tkFileDialog import askopenfilename,asksaveasfile
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
import os
import shutil


class PyApp():
    def __init__(self):
        self.NAME_FILE = "./file_origin/archivo.csv"
        self.NAME_FILE_SAVE = "./results/results.txt"
        self.lista_concatenada = []
        self.num_column_before = 0
        self.first = False
        self.counter  = 0
        self.root2 = ''
        self.root3 = ''
        self.file_result_final = open('./results/results.txt', 'w')

        #tk.Frame.__init__(self, *args, **kwargs)
        self.root = Tk()
        self.root.wm_title(u"Libre Estad�stica")
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon)

        menubar = Menu(self.root)

        try:
            filemenu = Menu(menubar, tearoff=0)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo", command=self.donothing)
            filemenu.add_command(label="Abrir archivo csv", command=self.importar_fichero_cvs)
            filemenu.add_command(label="Guardar Resultados", command=self.guardar)
            filemenu.add_command(label="Guardar Como...", command=self.donothing)
            filemenu.add_command(label="Cerrar", command=self.donothing)

            filemenu.add_separator()

            filemenu.add_command(label="Salir", command=self.close)
            menubar.add_cascade(label="Fichero", menu=filemenu)


            editmenu = Menu(menubar, tearoff=0)
            #editmenu.add_command(label="Undo", command=self.donothing)



            #editmenu.add_separator()

            centralmenu = Menu(editmenu, tearoff=0)
            centralmenu.add_command(label=u"Media aritm�tica", command=self.media_aritmetica)
            centralmenu.add_command(label=u"Suma", command=self.suma)
            centralmenu.add_command(label=u"Mediana", command=self.mediana)
            centralmenu.add_command(label=u"Moda", command=self.moda)

            dipersionmenu = Menu(editmenu, tearoff=0)
            dipersionmenu.add_command(label=u"Varianza", command=self.varianza)
            dipersionmenu.add_command(label=u"Desviaci�n T�pica", command=self.desviacion_tipica)
            dipersionmenu.add_command(label=u"Rango", command=self.rango)
            dipersionmenu.add_command(label=u"M�nimo", command=self.minimo)

            editmenu.add_cascade(label="Medidas Tendencia Central", menu=centralmenu)
            editmenu.add_cascade(label=u"Medidas Dispersi�n", menu=dipersionmenu)
            editmenu.add_command(label="Paste", command=self.donothing)
            editmenu.add_command(label="Delete", command=self.donothing)
            editmenu.add_command(label="Select All", command=self.donothing)

            menubar.add_cascade(label="Editar", menu=editmenu)
            helpmenu = Menu(menubar, tearoff=0)
            helpmenu.add_command(label="Help Index", command=self.donothing)
            helpmenu.add_command(label="About...", command=self.donothing)
            menubar.add_cascade(label="Help", menu=helpmenu)

            self.root.config(menu=menubar)
            self.root.mainloop()
        except:
            self.root.destroy()

        '''
        super(PyApp, self).__init__()

        self.set_title(u"Libre Estad�stica")
        self.set_size_request(300, 70)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        self.NAME_FILE = "archivo.csv"
        self.lista_concatenada = []
        self.num_column_before = 0
        self.first = False

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        imenu = gtk.Menu()
        importm = gtk.MenuItem("Import")
        importm.set_submenu(imenu)
        inews = gtk.MenuItem("Importar fichero cvs...")
        inews.connect("activate", self.importar_fichero_cvs, None)
        ibookmarks = gtk.MenuItem("Probando hija...")
        ibookmarks.connect("activate", self.probando_hija, None)
        imail = gtk.MenuItem("Import mail...")
        imenu.append(inews)
        imenu.append(ibookmarks)
        imenu.append(imail)
        filemenu.append(importm)

        mb.append(filem)

        toolmenu = gtk.Menu()
        toolm = gtk.MenuItem("Herramientas")
        toolm.set_submenu(toolmenu)

        imenu_two = gtk.Menu()
        mediam = gtk.MenuItem(u"Medidas Tendencia Central")
        mediam.set_submenu(imenu_two)
        mediam_sub = gtk.MenuItem(u"Media aritm�tica")
        modam_sub = gtk.MenuItem(u"Mediana")
        mediam_sub.connect("activate", self.media_aritmetica, None)
        modam_sub.connect("activate", self.mediana, None)

        imenu_three = gtk.Menu()
        dispersionm = gtk.MenuItem(u"Medidas Dispersi�n")
        dispersionm.set_submenu(imenu_three)
        dispersionm_sub = gtk.MenuItem(u"Rango")
        variancem_sub = gtk.MenuItem(u"Varianza")
        desviacionm_sub = gtk.MenuItem(u"Desviaci�n T�pica")
        dispersionm_sub.connect("activate", self.rango, None)
        variancem_sub.connect("activate", self.varianza, None)
        desviacionm_sub.connect("activate", self.desviacion_tipica, None)
        imenu_three.append(dispersionm_sub)
        imenu_three.append(variancem_sub)
        imenu_three.append(desviacionm_sub)
        imenu_two.append(mediam_sub)
        imenu_two.append(modam_sub)
        toolmenu.append(mediam)
        toolmenu.append(dispersionm)
        mb.append(toolm)

        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
    '''
    def close(self):
        self.root.destroy()


    def donothing(self):
        '''
        filewin = Toplevel(self.root)
        self.root.title("Resul ")
        button = Button(filewin, text="Do nothing button")
        button.pack()
        
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_deviation = self.calcular_desviacion_tipica(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Desviaci�n T�pica para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_deviation)
            self.lista_concatenada.append(cadena)

        self.root = Tk()
        self.root.title("Resultado ")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root)
        T = Text(self.root, height=10, width=100)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        T.grab_set()
        T.focus_set()
        T.see(END)
        T.config(state='disabled')
        self.root.mainloop()
        '''
        self.counter += 1
        t = Toplevel(self.root)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def probando_hija(self, widget, data=None):
        print "PRObando hija"

    def minimo(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_minimo = self.calcular_minimo(csvarchivo.as_matrix()[:, i])
            cadena = str(u"M�nimo para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_minimo)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.deiconify()
            self.root2.destroy()
            self.root2.quit()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()
        #self.root2.destroy()


    def calcular_minimo(self, value_matrix):
        return np.amin(value_matrix)

    def moda(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_moda = self.calcular_moda(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Moda para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_moda)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.deiconify()
            self.root2.destroy()
            self.root2.quit()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()
        #self.root2.destroy()


    def calcular_moda(self, value_matrix):
        result_moda = stats.mode(value_matrix)[0]
        result_moda = str(result_moda).replace("[", "")
        result_moda = str(result_moda).replace("]", "")
        result_moda = str(result_moda).replace(".", "")

        return float(result_moda)

    def mediana(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_median = self.calcular_mediana(csvarchivo.as_matrix()[:, i])
            print csvarchivo.as_matrix()[:, i]
            cadena = str(u"Mediana para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_median)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.deiconify()
            self.root2.destroy()
            self.root2.quit()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()
        #self.root2.destroy()


    def calcular_mediana(self, value_matrix):
        return np.median(value_matrix)


    def suma(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_suma = self.calcular_suma(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Suma para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_suma)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.deiconify()
            self.root2.destroy()
            self.root2.quit()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()
        #self.root2.destroy()


    def calcular_suma(self, value_matrix):
        return np.sum(value_matrix)


    def desviacion_tipica(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_deviation = self.calcular_desviacion_tipica(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Desviaci�n T�pica para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_deviation)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.deiconify()
            self.root2.destroy()
            self.root2.quit()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()
        #self.root2.destroy()


    def calcular_desviacion_tipica(self, value_matrix):
        return np.std(value_matrix)


    def varianza(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_variance= self.calcular_varianza(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Varianza para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_variance)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.quit()
            self.root2.destroy()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        # self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()


    def calcular_varianza(self,value_matrix):
        return np.var(value_matrix)


    def media_aritmetica(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0,num_column):
            cadena = str(u"Media Aritm�tica para ")+str(csvarchivo.columns[i])+str(u' = ')+str(np.average(csvarchivo.as_matrix()[:,i]))
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.quit()
            self.root2.destroy()
            self.file_result_final = open('./results/results.txt', 'w')


        self.root2 = Toplevel(self.root)

        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()

        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)

        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        quote = ''

        for i in range (0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        #T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()


    def rango(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            matrix = np.matrix(csvarchivo.as_matrix()[:,i])
            valor_maximo = matrix.max()
            valor_minimo = matrix.min()
            rango = self.calcular_rango(valor_maximo, valor_minimo)
            cadena = str(u"Rango para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(rango)
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.destroy()
            self.file_result_final = open('./results/results.txt', 'w')

        self.root2 = Toplevel(self.root)
        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"./images/lararov_6.gif")
        self.root2.tk.call('wm', 'iconphoto', self.root2._w, icon)
        #self.root2.iconify()
        self.root2.deiconify()

        screen_width = self.root2.winfo_screenwidth()
        screen_height = self.root2.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root2.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(self.root2)
        T = Text(self.root2, height=10, width=100)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = ''

        for i in range(0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        self.file_result_final.write(quote)
        self.file_result_final.close()
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()


    def calcular_rango(self,valor_maximo, valor_minimo):
        rango = valor_maximo - valor_minimo
        return rango


    def guardar(self):
        file = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        file_two =  str(file).split(',')[0]
        file_two = str(file_two).replace("<open file '",'')
        file_final = str(file_two).replace("'", '')
        shutil.copy(self.NAME_FILE_SAVE, file_final)
        # text2save = str(text.get(1.0, END))  # starts from `1.0`, not `0.0`
        # f.write(text2save)
        # f.close()  # `()` was missing.


    def importar_fichero_cvs(self):
            #try:
                # Make a top-level instance and hide since it is ugly and big.
                '''
                self.root3 = Tkinter.Tk()
                self.root3.withdraw()

                # Make it almost invisible - no decorations, 0 size, top left corner.
                self.root3.overrideredirect(True)
                self.root3.geometry('0x0+0+0')

                # Show window again and lift it to top so it can get focus,
                # otherwise dialogs will end up behind the terminal.
                self.root3.deiconify()
                self.root3.lift()
                self.root3.focus_force()
                '''
                filenames = tkFileDialog.askopenfilenames(parent=self.root,filetypes=[("Archivos CSV",".csv")])  # Or some other dialog
                filenames = str(filenames).replace("',)", "")
                filenames = str(filenames).replace("('", "")
                shutil.copy(filenames, self.NAME_FILE)

                #self.root3.destroy()
                # Get rid of the top-level instance once to make it actually invisible.
                #self.root.destroy()
            #except:
                #pass
                #print "llegamos aqui Salimos"
                #self.root3.destroy()


if __name__ == "__main__":
    PyApp()


