import PySimpleGUI as pysg
import time
from functions import *

pysg.theme('SandyBeach')

label1 = pysg.Text('Select files:')
input1 = pysg.Input(key='files_input')
choose_button1 = pysg.FilesBrowse('Choose...', key='files')
label2 = pysg.Text('Add file name (or autogenerated):')
input2 = pysg.Input(key='file_name')
label3 = pysg.Text('Select destination folder:')
input3 = pysg.Input(pathlib.Path.cwd())
choose_button3 = pysg.FolderBrowse('Choose...', key='dest')

cmprss_button = pysg.Button('Process')
label_success = pysg.Text(key='label_success', text_color='dark blue')


layout = [[label1, input1, choose_button1],
          [label2, input2],
          [label3, input3, choose_button3],
          [cmprss_button, label_success]]

window = pysg.Window('Srts to txt', layout=layout, font=('Helvetica', 15))

while True:
    event, value = window.read()
    if event == pysg.WINDOW_CLOSED:
        break
    paths = value['files'].split(';')
    dest = value['dest']
    name = value['file_name']
    if not paths[0]:
        pysg.popup('Select some .srt files first', text_color='dark blue')
        continue
    clean_and_merge(paths, dest, name)
    window['label_success'].update(value='txt created')

    time.sleep(5)
    window['label_success'].update(value='')
    window['files_input'].update(value='')

window.close()