#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.grid
from random import *

class Page3Frame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)

		self.SetSize((1000, 562))
		self.SetMinSize((1000, 500))
		self.SetMaxSize((1000, 500))

		self.panel_1 = wx.Panel(self, wx.ID_ANY)

		self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY)
		self.grid_1.CreateGrid(4, 6)
		self.grid_1.SetColLabelSize(0)
		self.grid_1.SetRowLabelSize(0)
		width = 500
		for col in range(6):
			self.grid_1.SetColSize(col, width / (6 + 1))
		self.grid_1.EnableEditing(False)

		self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_3 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_4 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_5 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_6 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_7 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_8 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.text_ctrl_9 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.btn_page4 = wx.Button(self, wx.ID_ANY, u"\u0414\u0430\u043b\u0435\u0435")

		self.__do_layout()
		self.zapoln_table()

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		grid_sizer_2 = wx.GridBagSizer(0, 0)
		self.grid_sizer_1 = wx.FlexGridSizer(0, 1, 0, 0)
		label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Исходные данные для расчёта:")
		label_2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(label_2, 0, wx.ALL, 10)
		label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Состав транспортного потока:")
		label_4.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(label_4, 0, wx.ALL, 10)
		label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 60%")
		self.grid_sizer_1.Add(label_5, 0, 0, 0)
		label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 35%")
		self.grid_sizer_1.Add(label_6, 0, 0, 0)
		label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автобусы - 3%")
		self.grid_sizer_1.Add(label_7, 0, 0, 0)
		label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автопоезда - 2%")
		self.grid_sizer_1.Add(label_8, 0, 0, 0)
		label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Коэффициенты приведения:")
		label_9.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(label_9, 0, wx.ALL, 10)
		label_10 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 1 ")
		label_10.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(label_10, 0, 0, 0)
		label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 1.5")
		label_11.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(label_11, 0, 0, 0)
		label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автобусы -  2.5")
		label_12.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(label_12, 0, 0, 0)
		label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автопоезда -  3", style=wx.ALIGN_LEFT)
		label_13.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(label_13, 0, 0, 0)
		label_14 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Таблица интенсивности а/м по наравлениям")
		label_14.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(label_14, 0, wx.ALL, 10)

		self.grid_sizer_1.Add(self.grid_1, 1, wx.ALL | wx.EXPAND, 10)
		self.grid_sizer_1.Add((0, 0), 0, 0, 0)

		sizer_2.Add(self.grid_sizer_1, 1, wx.EXPAND | wx.SHAPED, 0)
		static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY, style=wx.LI_VERTICAL)
		sizer_2.Add(static_line_1, 0, wx.EXPAND, 0)
		label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Необходимо рассчитать:")
		label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		grid_sizer_2.Add(label_1, (0, 0), (1, 1), wx.ALL, 10)
		label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "N = a*Ni*x + b*Ni*y + c*Ni*z + d*Ni*w                    ")
		label_3.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		grid_sizer_2.Add(label_3, (1, 0), (1, 1), wx.ALL, 10)
		label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0433\u0434\u0435 N - \u0438\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c, \u0430\u0432\u0442/ \u0447\na,b,c,d -\u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u0438\u044f\nx,y,z - \u0434\u043e\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435\u0439")
		grid_sizer_2.Add(label_15, (2, 0), (1, 1), 0, 0)
		label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, "N1 = ")
		grid_sizer_2.Add(label_16, (3, 0), (1, 1), 0, 0)
		label_25 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_25, (3, 1), (1, 1), 0, 0)
		label_26 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_26, (3, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_1, (3, 3), (1, 1), 0, 0)
		bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_1.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_1, (3, 4), (1, 1), 0, 0)
		label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, "N11 = ")
		grid_sizer_2.Add(label_17, (4, 0), (1, 1), 0, 0)
		label_27 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_27, (4, 1), (1, 1), 0, 0)
		label_28 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_28, (4, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_2, (4, 3), (1, 1), 0, 0)
		bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_2.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_2, (4, 4), (1, 1), 0, 0)
		label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, "N12 = ")
		grid_sizer_2.Add(label_18, (5, 0), (1, 1), 0, 0)
		label_31 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_31, (5, 1), (1, 1), 0, 0)
		label_32 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_32, (5, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_3, (5, 3), (1, 1), 0, 0)
		bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_3.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_3, (5, 4), (1, 1), 0, 0)
		label_19 = wx.StaticText(self.panel_1, wx.ID_ANY, u"N1(\u043f\u0440\u044f\u043c\u043e) = ")
		grid_sizer_2.Add(label_19, (6, 0), (1, 1), 0, 0)
		label_29 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_29, (6, 1), (1, 1), 0, 0)
		label_30 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_30, (6, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_4, (6, 3), (1, 1), 0, 0)
		bitmap_4 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_4.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_4, (6, 4), (1, 1), 0, 0)
		label_20 = wx.StaticText(self.panel_1, wx.ID_ANY, "N2 = ")
		grid_sizer_2.Add(label_20, (7, 0), (1, 1), 0, 0)
		label_33 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_33, (7, 1), (1, 1), 0, 0)
		label_34 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_34, (7, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_5, (7, 3), (1, 1), 0, 0)
		bitmap_5 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_5.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_5, (7, 4), (1, 1), 0, 0)
		label_21 = wx.StaticText(self.panel_1, wx.ID_ANY, "N21 =")
		grid_sizer_2.Add(label_21, (8, 0), (1, 1), 0, 0)
		label_35 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_35, (8, 1), (1, 1), 0, 0)
		label_36 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_36, (8, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_6, (8, 3), (1, 1), 0, 0)
		bitmap_6 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_6.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_6, (8, 4), (1, 1), 0, 0)
		label_22 = wx.StaticText(self.panel_1, wx.ID_ANY, "N22 =")
		grid_sizer_2.Add(label_22, (9, 0), (1, 1), 0, 0)
		label_37 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_37, (9, 1), (1, 1), 0, 0)
		label_38 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_38, (9, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_7, (9, 3), (1, 1), 0, 0)
		bitmap_7 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_7.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_7, (9, 4), (1, 1), 0, 0)
		label_23 = wx.StaticText(self.panel_1, wx.ID_ANY, u"N2(\u043f\u0440\u044f\u043c\u043e) =")
		grid_sizer_2.Add(label_23, (10, 0), (1, 1), 0, 0)
		label_39 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_39, (10, 1), (1, 1), 0, 0)
		label_40 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_40, (10, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_8, (10, 3), (1, 1), 0, 0)
		bitmap_8 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_8.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_8, (10, 4), (1, 1), 0, 0)
		label_24 = wx.StaticText(self.panel_1, wx.ID_ANY, "N3 =")
		grid_sizer_2.Add(label_24, (11, 0), (1, 1), 0, 0)
		label_41 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_41, (11, 1), (1, 1), 0, 0)
		label_42 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(label_42, (11, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_9, (11, 3), (1, 1), 0, 0)
		bitmap_9 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg", wx.BITMAP_TYPE_ANY))
		bitmap_9.SetMinSize((35, 35))
		grid_sizer_2.Add(bitmap_9, (11, 4), (1, 1), 0, 0)
		sizer_2.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		self.panel_1.SetSizer(sizer_2)

		sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
		sizer_1.Add(self.btn_page4, 0, wx.ALIGN_RIGHT, 0)

		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade
	def zapoln_table(self):
		rows = self.grid_1.GetNumberRows()
		cols = self.grid_1.GetNumberCols()
		
		self.grid_1.SetCellValue(0, 0, "N1")
		self.grid_1.SetCellValue(1, 0, "N11")
		self.grid_1.SetCellValue(2, 0, "N12")
		self.grid_1.SetCellValue(3, 0, "NП1")
		
		
		self.grid_1.SetCellValue(0, 2, "N2")
		self.grid_1.SetCellValue(1, 2, "N21")
		self.grid_1.SetCellValue(2, 2, "N22")
		self.grid_1.SetCellValue(3, 2, "NП2")
		
		self.grid_1.SetCellValue(0, 4, "N3")
		self.grid_1.SetCellValue(1, 4, "N31")
		self.grid_1.SetCellValue(2, 4, "N32")
		self.grid_1.SetCellValue(3, 4, "NП3")
		
		self.grid_1.SetCellValue(0, 4, "N4")
		self.grid_1.SetCellValue(1, 4, "N41")
		self.grid_1.SetCellValue(2, 4, "N42")
		self.grid_1.SetCellValue(3, 4, "NП4")
		
		for i in range(cols):
			for j in range(rows):
				if not i % 2 ==0:
					s0 = int(random() * 1000)
					self.grid_1.SetCellValue(j, i, str(s0))
		
		

		
		for i in range(cols):
			for j in range(rows):
				if i % 2 == 0:
					self.grid_1.SetCellFont(j, i, wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
					
			
			
			
		
		
		

		
		
	
# end of class MyFrame

class Page3(wx.App):
	def OnInit(self):
		self.frame = Page3Frame(None, wx.ID_ANY, "")
		self.frame.Show()
		return True

# end of class MyApp

if __name__ == "__main__":
	app = Page3(0)
	app.MainLoop()
