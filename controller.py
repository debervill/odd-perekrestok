import os
import tkinter as tk
import wx

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def setBacgroundColor():
    """
    Устанавливает цвет панели для приложения
    :return:
    """
    hex_color = "#DBF0B2"
    color =hex_to_rgb(hex_color)
    
    return color

def setBckgroundButtonColor():
    # todo Найти все кнопки в панели и установить им цвет
    """
    Устанавливает цвет кнопок
    :return:
    """
    hex_color = "#F8B8B8"
    color = hex_to_rgb(hex_color)

    return color
    
def getFullPath(file):
    put = os.getcwd()
    path = str(put) + '\\' + file
    return path


def setFrameSize():
    """
    :parameter sh,sw - ширина и высота экрана, на котором
    запускается программа
    :return: w,h - размеры фрейма для отрисовки gui
    """
    root = tk.Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    w,h = int(0.75 * sw),  int(0.75 * sh)

    if w < 800 and h < 600:
        w, h = 800, 600
        
    return w, h
