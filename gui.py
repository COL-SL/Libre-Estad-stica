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
from Tkinter import *
import statistics as st


class PyApp(gtk.Window):
    def __init__(self):
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
        T.grab_set()
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


    def media_aritmetica(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0,num_column):
            cadena = str(u"Media Aritmética para ")+str(csvarchivo.columns[i])+str(u' = ')+str(np.average(csvarchivo.as_matrix()[:,i]))
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

        for i in range (0, len(self.lista_concatenada)):
            if i == self.num_column_before and self.first == True:
                quote = quote + '\n'
            quote = quote + self.lista_concatenada[i]
            quote = quote + '\n'

        self.num_column_before = self.num_column_before + num_column
        self.first = True
        T.insert(END, quote)
        T.see(END)
        T.config(state='disabled')
        root.mainloop()


    def rango(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0, num_column):
            matrix = np.matrix(csvarchivo.as_matrix()[:,i])
            valor_maximo = matrix.max()
            valor_minimo = matrix.min()
            rango = self.calcular_rango(valor_maximo, valor_minimo)
            cadena = str(u"Rango para ") + str(csvarchivo.columns[i]) + str(u' = ') + str(rango)
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


    def calcular_rango(self,valor_maximo, valor_minimo):
        rango = valor_maximo - valor_minimo
        return rango


    def importar_fichero_cvs(self, widget, data=None):
        dialog = gtk.FileChooserDialog("Abrir..",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            extension = dialog.get_filename().split('.')[-1]
        if response == gtk.RESPONSE_OK and extension == 'csv':
            filename = dialog.get_filename()
            copyfile(filename, self.NAME_FILE)
        elif response != gtk.RESPONSE_CANCEL and response != gtk.RESPONSE_DELETE_EVENT:
            md = gtk.MessageDialog(self,
                                   gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR,
                                   gtk.BUTTONS_CLOSE, "Formato de archivo incorrecto")
            md.run()
            md.destroy()
        dialog.destroy()


PyApp()
gtk.main()