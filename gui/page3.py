#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.grid
from random import *

class Page3Frame(wx.Frame):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)

		self.SetSize((1000, 700))
		self.SetMinSize((1000, 700))
		self.SetMaxSize((1000, 700))

		self.panel_1 = wx.Panel(self, wx.ID_ANY)

		self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY)
		self.grid_1.CreateGrid(4, 8)
		self.grid_1.SetColLabelSize(0)
		self.grid_1.SetRowLabelSize(0)
		width = 500
		for col in range(8):
			self.grid_1.SetColSize(col, width / (8 + 1))
		self.grid_1.EnableEditing(False)

		self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_1.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda1)
		self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_2.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda2)
		self.text_ctrl_3 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_3.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda3)
		self.text_ctrl_4 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_4.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda4)
		self.text_ctrl_5 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_5.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda5)
		self.text_ctrl_6 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_6.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda6)
		self.text_ctrl_7 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_7.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda7)
		self.text_ctrl_8 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_8.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda8)
		self.text_ctrl_9 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_9.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda9)
		self.text_ctrl_10 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_10.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda10)
		self.text_ctrl_11 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_11.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda11)
		self.text_ctrl_12 = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_12.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda12)
		self.btn_page4 = wx.Button(self, wx.ID_ANY, u"\u0414\u0430\u043b\u0435\u0435")
		self.btn_page4.Bind(wx.EVT_BUTTON, self.gopage4)


		self.__do_layout()
		self.zapoln_table()
		self.get_raschet_in_right()


	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		grid_sizer_2 = wx.GridBagSizer(0, 0)
		self.grid_sizer_1 = wx.FlexGridSizer(0, 1, 0, 0)
		
		self.label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Исходные данные для расчёта:")
		self.label_2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
		self.label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Состав транспортного потока:")
		self.label_4.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
		self.label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 60%")
		self.grid_sizer_1.Add(self.label_5, 0, 0, 0)
		self.label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 35%")
		self.grid_sizer_1.Add(self.label_6, 0, 0, 0)
		self.label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автобусы - 3%")
		self.grid_sizer_1.Add(self.label_7, 0, 0, 0)
		self.label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автопоезда - 2%")
		self.grid_sizer_1.Add(self.label_8, 0, 0, 0)
		self.label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Коэффициенты приведения:")
		self.label_9.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(self.label_9, 0, wx.ALL, 10)
		self.label_10 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 1 ")
		self.label_10.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(self.label_10, 0, 0, 0)
		self.label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Легковые автомобили - 1.5")
		self.label_11.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(self.label_11, 0, 0, 0)
		self.label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автобусы -  2.5")
		self.label_12.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(self.label_12, 0, 0, 0)
		self.label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Автопоезда -  3", style=wx.ALIGN_LEFT)
		self.label_13.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
		self.grid_sizer_1.Add(self.label_13, 0, 0, 0)
		self.label_14 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Таблица интенсивности а/м по наравлениям")
		self.label_14.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.grid_sizer_1.Add(self.label_14, 0, wx.ALL, 10)

		self.grid_sizer_1.Add(self.grid_1, 1, wx.ALL | wx.EXPAND, 10)
		self.grid_sizer_1.Add((0, 0), 0, 0, 0)

		sizer_2.Add(self.grid_sizer_1, 1, wx.EXPAND | wx.SHAPED, 0)
		static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY, style=wx.LI_VERTICAL)
		sizer_2.Add(static_line_1, 0, wx.EXPAND, 0)
		self.label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Необходимо рассчитать:")
		self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		grid_sizer_2.Add(self.label_1, (0, 0), (1, 1), wx.ALL, 10)
		self.label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "N = a*Ni*x + b*Ni*y + c*Ni*z + d*Ni*w                    ")
		self.label_3.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		grid_sizer_2.Add(self.label_3, (1, 0), (1, 1), wx.ALL, 10)
		self.label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0433\u0434\u0435 N - \u0438\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c, \u0430\u0432\u0442/ \u0447\na,b,c,d -\u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u0438\u044f\nx,y,z - \u0434\u043e\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435\u0439")
		grid_sizer_2.Add(self.label_15, (2, 0), (1, 1), 0, 0)
		self.label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, "N1 = ")
		grid_sizer_2.Add(self.label_16, (3, 0), (1, 1), 0, 0)
		self.label_25 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_25, (3, 1), (1, 1), 0, 0)
		self.label_26 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_26, (3, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_1, (3, 3), (1, 1), 0, 0)
		
		self.bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_1.SetMinSize((35, 35))
		
		grid_sizer_2.Add(self.bitmap_1, (3, 4), (1, 1), 0, 0)
		self.label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, "N11 = ")
		grid_sizer_2.Add(self.label_17, (4, 0), (1, 1), 0, 0)
		self.label_27 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_27, (4, 1), (1, 1), 0, 0)
		self.label_28 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_28, (4, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_2, (4, 3), (1, 1), 0, 0)
		
		self.bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_2.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_2, (4, 4), (1, 1), 0, 0)
		
		self.label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, "N12 = ")
		grid_sizer_2.Add(self.label_18, (5, 0), (1, 1), 0, 0)
		self.label_31 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_31, (5, 1), (1, 1), 0, 0)
		self.label_32 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_32, (5, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_3, (5, 3), (1, 1), 0, 0)
		
		self.bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_3.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_3, (5, 4), (1, 1), 0, 0)
		
		self.label_19 = wx.StaticText(self.panel_1, wx.ID_ANY, u"N1(\u043f\u0440\u044f\u043c\u043e) = ")
		grid_sizer_2.Add(self.label_19, (6, 0), (1, 1), 0, 0)
		self.label_29 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_29, (6, 1), (1, 1), 0, 0)
		self.label_30 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_30, (6, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_4, (6, 3), (1, 1), 0, 0)
		self.bitmap_4 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_4.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_4, (6, 4), (1, 1), 0, 0)
		
		self.label_20 = wx.StaticText(self.panel_1, wx.ID_ANY, "N2 = ")
		grid_sizer_2.Add(self.label_20, (7, 0), (1, 1), 0, 0)
		self.label_33 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_33, (7, 1), (1, 1), 0, 0)
		self.label_34 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_34, (7, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_5, (7, 3), (1, 1), 0, 0)
		self.bitmap_5 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_5.SetMinSize((35, 35))
		
		grid_sizer_2.Add(self.bitmap_5, (7, 4), (1, 1), 0, 0)
		self.label_21 = wx.StaticText(self.panel_1, wx.ID_ANY, "N21 =")
		grid_sizer_2.Add(self.label_21, (8, 0), (1, 1), 0, 0)
		self.label_35 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_35, (8, 1), (1, 1), 0, 0)
		self.label_36 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_36, (8, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_6, (8, 3), (1, 1), 0, 0)
		self.bitmap_6 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_6.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_6, (8, 4), (1, 1), 0, 0)
		
		self.label_22 = wx.StaticText(self.panel_1, wx.ID_ANY, "N22 =")
		grid_sizer_2.Add(self.label_22, (9, 0), (1, 1), 0, 0)
		self.label_37 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_37, (9, 1), (1, 1), 0, 0)
		self.label_38 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_38, (9, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_7, (9, 3), (1, 1), 0, 0)
		self.bitmap_7 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_7.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_7, (9, 4), (1, 1), 0, 0)
		self.label_23 = wx.StaticText(self.panel_1, wx.ID_ANY, u"N2(\u043f\u0440\u044f\u043c\u043e) =")
		grid_sizer_2.Add(self.label_23, (10, 0), (1, 1), 0, 0)
		self.label_39 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_39, (10, 1), (1, 1), 0, 0)
		self.label_40 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_40, (10, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_8, (10, 3), (1, 1), 0, 0)
		self.bitmap_8 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_8.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_8, (10, 4), (1, 1), 0, 0)
		
		self.label_24 = wx.StaticText(self.panel_1, wx.ID_ANY, "N3 =")
		grid_sizer_2.Add(self.label_24, (11, 0), (1, 1), 0, 0)
		self.label_41 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_41, (11, 1), (1, 1), 0, 0)
		self.label_42 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
		grid_sizer_2.Add(self.label_42, (11, 2), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_9, (11, 3), (1, 1), 0, 0)
		self.bitmap_9 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_9.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_9, (11, 4), (1, 1), 0, 0)
		
		self.label_100 = wx.StaticText(self.panel_1, wx.ID_ANY, "N31 =")
		grid_sizer_2.Add(self.label_100, (12, 0), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_10, (12, 3), (1, 1), 0, 0)
		self.bitmap_10 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_10.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_10, (12, 4), (1, 1), 0, 0)
		
		self.label_101 = wx.StaticText(self.panel_1, wx.ID_ANY, "N32 =")
		grid_sizer_2.Add(self.label_101, (13, 0), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_11, (13, 3), (1, 1), 0, 0)
		self.bitmap_11 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_11.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_11, (13, 4), (1, 1), 0, 0)
		
		self.label_102 = wx.StaticText(self.panel_1, wx.ID_ANY, "N3 прямо =")
		grid_sizer_2.Add(self.label_102, (14, 0), (1, 1), 0, 0)
		grid_sizer_2.Add(self.text_ctrl_12, (14, 3), (1, 1), 0, 0)
		self.bitmap_12 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("../img/bad.jpg", wx.BITMAP_TYPE_ANY))
		self.bitmap_12.SetMinSize((35, 35))
		grid_sizer_2.Add(self.bitmap_12, (14, 4), (1, 1), 0, 0)
		

		
		sizer_2.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		self.panel_1.SetSizer(sizer_2)

		sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
		sizer_1.Add(self.btn_page4, 0, wx.ALIGN_RIGHT, 0)

		self.SetSizer(sizer_1)
		self.Layout()
	
	def scale_bitmap(self, bitmap, width, height):
		self.w = width
		self.h = height
		image = wx.Image(bitmap)
		image = image.Scale(self.w, self.h, wx.IMAGE_QUALITY_HIGH)
		result = wx.Bitmap(image)
		return result


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
		
	
		self.grid_1.SetCellValue(0, 6, "N4")
		self.grid_1.SetCellValue(1, 6, "N41")
		self.grid_1.SetCellValue(2, 6, "N42")
		self.grid_1.SetCellValue(3, 6, "NП4")
		
		for i in range(cols):
			for j in range(rows):
				if not i % 2 ==0:
					s0 = int(random() * 1000)
					self.grid_1.SetCellValue(j, i, str(s0))

		for i in range(cols):
			for j in range(rows):
				if i % 2 == 0:
					self.grid_1.SetCellFont(j, i, wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
	
	def raschet(self, intens):
		"""
		:param
		self.intens  - интенсивность транспортного потока
		self.legk- состав транспортного потока
		self.k_legk - коэффициенты приведения
		"""
		self.intense = int(intens)
		
		self.legk = 0.6
		self.gruz = 0.35
		self.avtobus = 0.03
		self.autopoezd = 0.02
		
		self.k_legk = 1
		self.k_gruz = 1.5
		self.k_avtobus = 2.5
		self.k_autopoezd = 3
		
		
		self.tmp_N1 = self.k_legk * self.intense * self.legk + self.k_gruz * self.intense * self.gruz + self.k_avtobus * self.intense * self.avtobus + self.k_autopoezd * self.intense * self.autopoezd
		self.N1 = "%.2f" % self.tmp_N1
		
		self.str_N1 = str(self.k_legk) + str('*') + str(self.intense) + str('*') + str(self.legk) +str('+') + \
		              str(self.k_gruz) +str('+') + str('*') + str(self.intense) +str('*') + str(self.gruz) + str('+') + \
		              str(self.k_avtobus) + str('*') + str(self.intense) + str('*') + str(self.avtobus) + str('+') + \
		              str(self.k_autopoezd) + str('*') + str(self.intense) + str('*') + str(self.autopoezd)
		
		
		return self.str_N1, self.N1
		
	def get_raschet_in_right(self):
		rows = self.grid_1.GetNumberRows()
		cols = self.grid_1.GetNumberCols()
		self.data = []
		for i in range(cols):
			for j in range(rows -1):
				if not i % 2 ==0:
					self.data.append(self.raschet(self.grid_1.GetCellValue(j, i)))
			
		self.label_16.SetLabel("N1 = " + str(self.data[0][0]) + "=")
		self.label_17.SetLabel("N11 = " + str(self.data[1][0]) + "=")
		self.label_18.SetLabel("N12 = " + str(self.data[2][0]) + "=")
		self.label_19.SetLabel("N1 прямо = " + str(self.data[0][1]) + "-" + str(self.data[1][1]) + "-" + str(self.data[2][1])  + "=")

		self.label_20.SetLabel("N2 =" + str(self.data[3][0]) + "=")
		self.label_21.SetLabel("N21 =" + str(self.data[4][0]) + "=")
		self.label_22.SetLabel("N22 =" + str(self.data[5][0]) + "=")
		self.label_23.SetLabel("N2 прямо = " + str(self.data[3][1]) + "-" + str(self.data[4][1]) + "-" + str(self.data[5][1])  + "=")
		
		self.label_24.SetLabel("N3 =" + str(self.data[6][0]) + "=")
		self.label_21.SetLabel("N31 =" + str(self.data[7][0]) + "=")
		self.label_22.SetLabel("N32 =" + str(self.data[8][0]) + "=")
		self.label_23.SetLabel("N3 прямо = " + str(self.data[3][1]) + "-" + str(self.data[4][1]) + "-" + str(self.data[5][1])  + "=")
		
		self.label_100.SetLabel("N4 =" + str(self.data[9][0]) + "=")
		self.label_101.SetLabel("N41 =" + str(self.data[10][0]) + "=")
		self.label_102.SetLabel("N42 =" + str(self.data[11][0]) + "=")
		self.label_23.SetLabel("N4 прямо = " + str(self.data[7][1]) + "-" + str(self.data[8][1]) + "-" + str(self.data[9][1]) + "=")
	
	def proverka_vvoda1(self, event):
		print(self.text_ctrl_1.GetValue())
		if len(self.text_ctrl_1.GetValue()) > 0:
			if self.text_ctrl_1.GetValue() == str(self.data[0][1]):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_1.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_1.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = ""
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_1.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_1.Show()
				self.text_ctrl_1.SetValue(str(self.data[0][1]))
				self.Refresh()

	def proverka_vvoda2(self, event):
		print(self.text_ctrl_2.GetValue())
		if len(self.text_ctrl_2.GetValue()) > 0:
			if self.text_ctrl_2.GetValue() == str(self.data[1][1]):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_2.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_2.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_2.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_2.Show()
				self.text_ctrl_2.SetValue(str(self.data[1][1]))
				self.Refresh()

	def proverka_vvoda3(self, event):
		print(self.text_ctrl_3.GetValue())
		if len(self.text_ctrl_3.GetValue()) > 0:
			if self.text_ctrl_3.GetValue() == str(self.data[2][1]):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_3.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_3.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_3.Show()
				self.text_ctrl_3.SetValue(str(self.data[2][1]))
				self.Refresh()

	def proverka_vvoda4(self, event):
		print(self.text_ctrl_4.GetValue())
		if len(self.text_ctrl_4.GetValue()) > 0:
			self.s = float(self.data[0][1]) - float(self.data[1][1])  - float(self.data[2][1])
			self.s1 = "%.2f" % self.s
			self.file = open("123", "a")
			self.file.writelines(self.s1)
			self.file.close()
			
			if self.text_ctrl_4.GetValue() == str(self.s1):

				print("good")
				print( str(float(self.data[0][1]) - float(self.data[1][1]) - float(self.data[2][1])))
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_4.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_4.Show()
				self.Refresh()
			else:
				print("bad")
			

				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_4.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_4.Show()
				self.s = float(self.data[0][1]) - float(self.data[1][1])  - float(self.data[2][1])
				self.s1 = "%.2f" % self.s
				self.text_ctrl_4.SetValue(str(self.s1))
				self.Refresh()

	def proverka_vvoda5(self, event):
		print(self.text_ctrl_5.GetValue())
		if len(self.text_ctrl_5.GetValue()) > 0:
			if self.text_ctrl_5.GetValue() == str(self.data[4][1]):
				print("good")
				
				self.img1 = "../img/123.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_5.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_5.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_5.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_5.Show()
				self.text_ctrl_5.SetValue(str(self.data[4][1]))
				self.Refresh()

	def proverka_vvoda6(self, event):
		print(self.text_ctrl_6.GetValue())
		if len(self.text_ctrl_6.GetValue()) > 0:
			if self.text_ctrl_6.GetValue() == str(self.data[5][1]):
				print("good")
			
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_6.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_6.Hide()
				self.Refresh()
			else:
				print("bad")
			
				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_6.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_6.Show()
				self.text_ctrl_6.SetValue(str(self.data[5][1]))
				self.Refresh()

	def proverka_vvoda7(self, event):
		print(self.text_ctrl_7.GetValue())
		if len(self.text_ctrl_7.GetValue()) > 0:
			if self.text_ctrl_7.GetValue() == str(self.data[6][1]):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_7.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_7.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = "../img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_7.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_7.Show()
				self.text_ctrl_7.SetValue(str(self.data[6][1]))
				self.Refresh()

	def proverka_vvoda8(self, event):
		print(self.text_ctrl_8.GetValue())
		if len(self.text_ctrl_8.GetValue()) > 0:
			self.s = float(self.data[3][1]) - float(self.data[4][1])- float(self.data[5][1])
			self.s1 = "%.2f" % self.s
			
			if self.text_ctrl_8.GetValue() == str(self.s1):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_8.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_8.Show()
				self.Refresh()
			else:
				print("bad")
				self.s = float(self.data[3][1]) - float(self.data[4][1])- float(self.data[5][1])
				self.s1 = "%.2f" % self.s
				self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_8.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_8.Show()
				self.text_ctrl_8.SetValue(str(self.s1))
				self.Refresh()

	def proverka_vvoda9(self, event):
		print(self.text_ctrl_9.GetValue())
		if len(self.text_ctrl_9.GetValue()) > 0:
			if self.text_ctrl_9.GetValue() == str(self.data[8][1]):
				print("good")
				
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_9.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_9.Show()
				self.Refresh()
			else:
				print("bad")
				
				self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_9.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_9.Show()
				self.text_ctrl_9.SetValue(str(self.data[8][1]))
				self.Refresh()

	def proverka_vvoda10(self, event):
		print(self.text_ctrl_10.GetValue())
		if len(self.text_ctrl_10.GetValue()) > 0:
			if self.text_ctrl_10.GetValue() == str(self.data[9][1]):
				print("good")
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_10.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_10.Show()
				self.Refresh()
			else:
				print("bad")
				1
				self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_10.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_10.Show()
				self.text_ctrl_10.SetValue(str(self.data[9][1]))
				self.Refresh()

	def proverka_vvoda11(self, event):
		print(self.text_ctrl_11.GetValue())
		if len(self.text_ctrl_11.GetValue()) > 0:
			if self.text_ctrl_11.GetValue() == str(self.data[10][1]):
				print("good")
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_11.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_11.Show()
				self.Refresh()
			else:
				print("bad")
				self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_11.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_11.Show()
				self.text_ctrl_11.SetValue(str(self.data[10][1]))
				self.Refresh()

	def proverka_vvoda12(self, event):
		print(self.text_ctrl_1.GetValue())
		if len(self.text_ctrl_1.GetValue()) > 0:
			self.s = float(self.data[7][1]) - float(self.data[8][1]) - float(self.data[9][1])
			self.s1 = "%.2f" % self.s
			if self.text_ctrl_1.GetValue() == str(self.s1):
				print("good")
				self.bitmap_1.Hide()
				self.img1 = "../img/bad.jpg"
				self.img4 = self.scale_bitmap(self.img1, 20, 20)
				self.bitmap_2.SetBitmap(wx.Bitmap(self.img4))
				self.bitmap_2.Show()
				self.Refresh()
			else:
				print("bad")
				self.s = float(self.data[7][1]) - float(self.data[8][1]) - float(self.data[9][1])
				self.s1 = "%.2f" % self.s  
				self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
				self.img3 = self.scale_bitmap(self.img2, 25, 25)
				self.bitmap_2.SetBitmap(wx.Bitmap(self.img3))
				self.bitmap_2.Show()
				self.text_ctrl_1.SetValue(str(self.s1))
				self.Refresh()
	def gopage4(self, event):
		#from gui import page4
		#page4.MyApp.OnInit(page4)
		#self.Destroy()
		pass



class Page3(wx.App):
	def OnInit(self):
		self.frame = Page3Frame(None, wx.ID_ANY, "")
		self.frame.Show()
		self.frame.Center()
		return True

# end of class MyApp

if __name__ == "__main__":
	app = Page3(0)
	app.MainLoop()
