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
from text_area import probando_clase as pc, text_area as ta

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title(u"Libre Estadística")
        self.set_size_request(450, 400)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        self.NAME_FILE = "archivo.csv"

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        imenu = gtk.Menu()
        importm = gtk.MenuItem("Import")
        importm.set_submenu(imenu)
        inews = gtk.MenuItem("Importar fichero cvs...")
        inews.connect("activate", self.importar_fichero_cvs, None)
        ibookmarks = gtk.MenuItem("Import bookmarks...")
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
        mediam_sub.connect("activate", self.media_aritmetica, None)

        imenu_three = gtk.Menu()
        dispersionm = gtk.MenuItem(u"Medidas Dispersión")
        dispersionm.set_submenu(imenu_three)
        dispersionm_sub = gtk.MenuItem(u"Rango")
        dispersionm_sub.connect("activate", self.rango, None)
        imenu_three.append(dispersionm_sub)
        imenu_two.append(mediam_sub)
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

    def media_aritmetica(self, widget, data=None):
        csvarchivo = pd.read_csv(self.NAME_FILE, encoding='utf-8')
        num_column = len(csvarchivo.columns)

        for i in range(0,num_column):
            print u"Media Aritmética para",csvarchivo.columns[i],'-->', np.average(csvarchivo.as_matrix()[:,i])

        mercedez = pc.Coche(0, 'Mercedez Benz', 15)
        mercedez.acelerar()

        X = ta.EntryExample()

    def rango(self, widget, data=None):
        print u"Rango"

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