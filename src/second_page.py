#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Sun Jun  6 15:00:40 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class SeconPageFrame(wx.Frame):
				def __init__(self, *args, **kwds):
								# begin wxGlade: SeconPageFrame.__init__
								kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
								wx.Frame.__init__(self, *args, **kwds)
								self.SetSize((800, 780))
								self.SetTitle("frame")

								sizer_1 = wx.BoxSizer(wx.VERTICAL)

								self.panel_1 = wx.Panel(self, wx.ID_ANY)
								sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

								sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "sizer_2"), wx.VERTICAL)

								label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Исходные данные для расчета\n")
								label_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
								sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)

								grid_sizer_1 = wx.GridSizer(0, 4, 0, 0)
								sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)

								label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория\nГоризональной улицы")
								grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER | wx.ALL, 10)

								label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER_HORIZONTAL)
								grid_sizer_1.Add(label_8, 0, wx.ALIGN_CENTER, 0)

								label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория \nВертикальной улицы")
								grid_sizer_1.Add(label_9, 0, wx.ALIGN_CENTER, 0)

								label_10 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
								grid_sizer_1.Add(label_10, 0, wx.ALIGN_CENTER, 0)

								label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос\nГоризонтальной улицы")
								grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER, 0)

								label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER_HORIZONTAL)
								grid_sizer_1.Add(label_12, 0, wx.ALIGN_CENTER, 0)

								label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос \nВертикальной улицы")
								grid_sizer_1.Add(label_13, 0, wx.ALIGN_CENTER, 0)

								label_14 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
								grid_sizer_1.Add(label_14, 0, wx.ALIGN_CENTER, 0)

								label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Выберите тип пересечения")
								label_18.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
								sizer_2.Add(label_18, 0, wx.ALL, 9)

								grid_sizer_3 = wx.GridSizer(0, 2, 0, 0)
								sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)

								self.radio_btn_2 = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Крестооборазный\n")
								grid_sizer_3.Add(self.radio_btn_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

								self.radio_btn_3 = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Т-образный")
								grid_sizer_3.Add(self.radio_btn_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

								bitmap_4 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("D:\\Programming\\PythonProjects\\odd-perekrestok\\img\\perekr4.jpg", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
								grid_sizer_3.Add(bitmap_4, 0, wx.ALIGN_CENTER, 0)

								bitmap_5 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("D:\\Programming\\PythonProjects\\odd-perekrestok\\img\\perekr-t.jpg", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
								grid_sizer_3.Add(bitmap_5, 0, wx.ALIGN_CENTER, 0)

								label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Необходимо расчитать:")
								label_15.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
								sizer_2.Add(label_15, 0, wx.ALL, 0)

								grid_sizer_2 = wx.FlexGridSizer(1, 9, 0, 0)
								sizer_2.Add(grid_sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 0)

								label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части\nГоризонтальной улицы")
								grid_sizer_2.Add(label_16, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 0)

								self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
								grid_sizer_2.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)

								bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("D:\\Programming\\PythonProjects\\odd-perekrestok\\img\\123.jpg", wx.BITMAP_TYPE_ANY))
								bitmap_2.Hide()
								grid_sizer_2.Add(bitmap_2, 0, 0, 0)

								label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части\nВертикальной улицы")
								grid_sizer_2.Add(label_17, 0, 0, 0)

								self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
								grid_sizer_2.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)

								bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("D:\\Programming\\PythonProjects\\odd-perekrestok\\img\\123.jpg", wx.BITMAP_TYPE_ANY))
								grid_sizer_2.Add(bitmap_3, 0, 0, 0)

								self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "button_1")
								sizer_2.Add(self.button_1, 0, wx.ALIGN_RIGHT, 0)

								self.panel_1.SetSizer(sizer_2)

								self.SetSizer(sizer_1)

								self.Layout()
								# end wxGlade

# end of class SeconPageFrame

class SecondPage(wx.App):
				def OnInit(self):
								self.frame = SeconPageFrame(None, wx.ID_ANY, "")
								self.SetTopWindow(self.frame)
								self.frame.Show()
								return True

# end of class SecondPage

if __name__ == "__main__":
				SeconPage = SecondPage(0)
				SeconPage.MainLoop()