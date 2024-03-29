import streamlit as st
import os
from functions import *

input1 = st.text_input('Add file name (or autogenerated):', key='file_name')
input2 = st.file_uploader('Select files:', key='files_input', accept_multiple_files=True)
# choose_button1 = pysg.FilesBrowse('Choose...', key='files')


def create_download_link(file_path, link_text):
    with open(file_path, "rb") as file:
        data = file.read()
    href = f"<a href='data:file/txt;base64,{data.decode('utf-8')}' download='{file_path}'>{link_text}</a>"
    return href


if input2:
    files = st.session_state['files_input']
    new_name = st.session_state['file_name']
    name = clean_and_merge(files, name=new_name)
    st.download_button('Download', data=open(name).read(), file_name=name)
