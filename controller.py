import os
import sys
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


def getSizeH():
    app = wx.App(False)
    sw, sh = wx.GetDisplaySize()
    w = 0.75 * sw
    h = 0.75 * sh
    app.Destroy()
    return w, h






