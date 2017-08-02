#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Copyright (C) 2017  Manuel David Jiménez Patiño

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
import statistics as st
from tkFileDialog import askopenfilename
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
import os



class PyApp():
    def __init__(self):
        self.NAME_FILE = "archivo.csv"
        self.lista_concatenada = []
        self.num_column_before = 0
        self.first = False
        self.counter  = 0
        self.root2 = ''
        self.root3 = ''

        #tk.Frame.__init__(self, *args, **kwargs)
        self.root = Tk()
        self.root.wm_title(u"Libre Estadística")
        icon = PhotoImage(file=r"/home/manueldavid/Escritorio/Programa_estadistica/lararov_6.gif")
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon)

        menubar = Menu(self.root)

        try:
            filemenu = Menu(menubar, tearoff=0)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo", command=self.donothing)
            filemenu.add_command(label="Abrir", command=self.importar_fichero_cvs)
            filemenu.add_command(label="Guardar", command=self.donothing)
            filemenu.add_command(label="Guardar Como...", command=self.donothing)
            filemenu.add_command(label="Cerrar", command=self.donothing)

            filemenu.add_separator()

            filemenu.add_command(label="Salir", command=self.close)
            menubar.add_cascade(label="Fichero", menu=filemenu)


            editmenu = Menu(menubar, tearoff=0)
            editmenu.add_command(label="Undo", command=self.donothing)



            editmenu.add_separator()

            centralmenu = Menu(editmenu, tearoff=0)
            centralmenu.add_command(label=u"Media aritmética", command=self.media_aritmetica)
            centralmenu.add_command(label=u"Rango", command=self.rango)

            editmenu.add_cascade(label="Medidas Tendencia Central", menu=centralmenu)
            editmenu.add_command(label=u"Medidas Dispersión", command=self.donothing)
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
            pass
            self.root.destroy()

        '''
        super(PyApp, self).__init__()

        self.set_title(u"Libre Estadística")
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
        mediam_sub = gtk.MenuItem(u"Media aritmética")
        modam_sub = gtk.MenuItem(u"Mediana")
        mediam_sub.connect("activate", self.media_aritmetica, None)
        modam_sub.connect("activate", self.mediana, None)

        imenu_three = gtk.Menu()
        dispersionm = gtk.MenuItem(u"Medidas Dispersión")
        dispersionm.set_submenu(imenu_three)
        dispersionm_sub = gtk.MenuItem(u"Rango")
        variancem_sub = gtk.MenuItem(u"Varianza")
        desviacionm_sub = gtk.MenuItem(u"Desviación Típica")
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
            cadena = str(u"Desviación Típica para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_deviation)
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

    def desviacion_tipica(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_deviation = self.calcular_desviacion_tipica(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Desviación Típica para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_deviation)
            self.lista_concatenada.append(cadena)

        root = Tk()
        root.title("Resultado ")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(root)
        T = Text(root, height=10, width=100)
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
        #T.grab_set()
        T.focus_set()
        T.see(END)
        T.config(state='disabled')
        root.mainloop()


    def calcular_desviacion_tipica(self, value_matrix):
        return np.std(value_matrix)


    def varianza(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_variance= self.calcular_varianza(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Varianza para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_variance)
            self.lista_concatenada.append(cadena)

        root = Tk()
        root.title("Resultado ")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(root)
        T = Text(root, height=10, width=100)
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
        T.focus_set()
        T.see(END)
        T.config(state='disabled')
        #self.root2.destroy()
        root.mainloop()


    def calcular_varianza(self,value_matrix):
        return np.var(value_matrix)


    def mediana(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            result_median = self.calcular_mediana(csvarchivo.as_matrix()[:, i])
            cadena = str(u"Mediana para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(result_median)
            self.lista_concatenada.append(cadena)

        root = Tk()
        root.title("Resultado ")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        width = 600
        height = 200

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        S = Scrollbar(root)
        T = Text(root, height=10, width=100)
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
        T.focus_set()
        T.see(END)
        T.config(state='disabled')
        root.mainloop()


    def calcular_mediana(self,value_matrix):
        return float(np.median(value_matrix))


    def media_aritmetica(self):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0,num_column):
            cadena = str(u"Media Aritmética para ")+str(csvarchivo.columns[i])+str(u' = ')+str(np.average(csvarchivo.as_matrix()[:,i]))
            self.lista_concatenada.append(cadena)

        self.counter += 1

        if self.first == True:
            self.root2.destroy()

        self.root2 = Toplevel(self.root)
        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"/home/manueldavid/Escritorio/Programa_estadistica/lararov_6.gif")
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

        self.root2 = Toplevel(self.root)
        self.root2.title("Resultado #%s" % self.counter)
        icon = PhotoImage(file=r"/home/manueldavid/Escritorio/Programa_estadistica/lararov_6.gif")
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
        T.see(END)
        # T.grab_set()
        T.config(state='disabled')
        self.root.mainloop()


    def calcular_rango(self,valor_maximo, valor_minimo):
        rango = valor_maximo - valor_minimo
        return rango


    def importar_fichero_cvs(self):
            try:
                # Make a top-level instance and hide since it is ugly and big.
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

                filenames = tkFileDialog.askopenfilenames(parent=self.root)  # Or some other dialog
                print filenames
                self.root3.destroy()

                # Get rid of the top-level instance once to make it actually invisible.
                #self.root.destroy()
            except:
                #pass
                print "llegamos aqui Salimos"
                self.root3.destroy()


if __name__ == "__main__":
    PyApp()


