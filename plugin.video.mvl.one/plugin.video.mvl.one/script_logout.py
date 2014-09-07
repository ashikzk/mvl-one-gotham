import xbmc, xbmcgui
import os

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'userdata', 'ZpMqXoNw')
if os.path.exists(file_path):
   os.remove(file_path)

xbmc.executebuiltin('Quit()')