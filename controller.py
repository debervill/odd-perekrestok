import os
import tkinter as tk
import wx

def setBacgroundColor():
    """
    Устанавливает цвет панели для приложения
    :return:
    """
    color  = "white"
    return color

def setBckgroundButtonColor():
    # todo Найти все кнопки в панели и установить им цвет
    """
    Устанавливает цвет кнопок
    :return:
    """
    wx.lib.colourdb.updateColourDB()
    color = wx.NamedColour("light coral")
    return color

def getFullPath(file):
    put = os.getcwd()
    path = str(put) + '\\' + file
    return path


def setSize():
    """
    :parameter sh,sw - ширина и высота экрана, на котором
    запускается программа
    :return: w,h - размеры фрейма для отрисовки gui
    """
    root = tk.Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    w = int(0.75 * sw)
    h = int(0.75 * sh)

    if w < 800 and h < 600:
        w, h = 800, 600
    return w, h
