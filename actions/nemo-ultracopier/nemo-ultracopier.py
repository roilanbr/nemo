#! /usr/bin/python
# -*- coding: utf-8 -*-

# ===========================
# Importar modulos
# ===========================

import os
os.system("clear")

import sys
from urllib import parse 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# ===========================
# Ejecución
# ===========================

# Guardar en variable el portapapeles e imprimir en formato de memoria
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clipboard = clipboard.wait_for_contents(Gdk.Atom.intern("x-special/gnome-copied-files", False))
print(f'\nClipboard :', clipboard, "\n")

# Imprimir para ir biendo lo que hay en el portapapeles
print(f'Clipboard :', clipboard.get_data(), "\n")                # Inprimir en formato legible por humanos

# Si lo que hay en "clipboard" no es "None" ejecutar lo siguiente
if clipboard is not None:
    # Convertir los saltos de líneas(splitlines) en formato de lista
    info = clipboard.get_data().splitlines()

    # Guardar la acción (copy, cut) realizada en el explorador "nemo"
    action = parse.unquote(info[0], encoding="utf-8", errors="remplace")
    files = info[1:]                            # Coger la ruta al archivo
    
    # Imprimir info, action y ruta
    print(f"Info      :", info)
    print(f'Action    :', action)
    print(f'Files     :', files, "\n")

    # Crear variable vacía
    file_list = ""

    # Bucle para cada elemento(file) en "files"
    for file in files:
        # Imprimir  ruta completa incluido "file://"
        print(f"Ruta:", file)       
        
        # Tomar la parte de la ruta despues de "file://" 
        # y convierte cataracteres tipo "%xx" a caracteres utf-8
        file = parse.unquote(file[7:], encoding="utf-8", errors="remplace")
        
        # Agregar las comillas y concatenar las rutas de los archivos
        file_list += "\"" + file + "\" "

    # Print la lista de los archivos concatenados
    print(f"Lista de archivos a copiar:\n{file_list}")

    if action == "copy":
        print("COPY")
        os.system(f"ultracopier cp {file_list} \"{sys.argv[1]}\"")
    elif action == "cut":
        os.system(f"ultracopier mv {file_list} \"{sys.argv[1]}\"")
        print("CUT")