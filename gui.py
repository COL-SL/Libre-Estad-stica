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

import gtk


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title(u"Libre Estadística")
        self.set_size_request(450, 400)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        imenu = gtk.Menu()
        importm = gtk.MenuItem("Import")
        importm.set_submenu(imenu)
        inews = gtk.MenuItem("Importar fichero cvs...")
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
        mediam = gtk.MenuItem(u"Media Aritmética")
        mediam.connect("activate", self.media_aritmetica, None)
        desviacionm = gtk.MenuItem(u"Desviación Típica")
        desviacionm.connect("activate", self.desviacion_tipica, None)
        toolmenu.append(mediam)
        toolmenu.append(desviacionm)
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
        print u"Calculamos Media Aritmética"

    def desviacion_tipica(self, widget, data=None):
        print u"Calculamos Desviación Típica"


PyApp()
gtk.main()