# -*- coding: UTF-8 -*-
import wx
import controller
from db.models import Student
from sqlalchemy import exists
from db.models import Session
from gui import SecondPage

import logging
import os

logging.basicConfig(filename="app.log",
							filemode='a',
							format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
							datefmt='%H:%M:%S',
							level=logging.DEBUG)

logging.info("Running Urban Planning")


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.panel_1 = wx.Panel(self, wx.ID_ANY)
		self.inpt_name = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.inpt_familia = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.inpt_group = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.inpt_zachetka = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		self.btn_settings = wx.Button(self.panel_1, wx.ID_ANY, u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438")
		self.btn_next = wx.Button(self.panel_1, wx.ID_ANY, u"\u0414\u0430\u043b\u0435\u0435")

		self.btn_settings.Bind(wx.EVT_BUTTON, self.setup)
		self.btn_next.Bind(wx.EVT_BUTTON, self.go_page2)

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("Расчет цикла свеетофорного регулирования: Приветственая")
		self.inpt_name.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.inpt_familia.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.inpt_zachetka.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		self.btn_settings.SetMinSize((100, 50))
		self.btn_next.SetMinSize((100, 50))
		#self.frameSize = controller.setSize()
		#elf.SetSize(self.frameSize)
		self.SetMinSize((800, 600))
		self.color = controller.setBacgroundColor()
		self.panel_1.SetBackgroundColour(self.color)

		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, ""), wx.VERTICAL)
		grid_sizer_2 = wx.GridSizer(0, 2, 0, 0)
		grid_sizer_1 = wx.GridSizer(0, 2, 0, 0)
		label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u0438  \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f\"")
		label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		sizer_2.Add(label_1, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.RIGHT, 20)
		label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0446\u0438\u043a\u043b\u0430 \u0441\u0432\u0435\u0442\u043e\u0444\u043e\u0440\u043d\u043e\u0433\u043e \u0440\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043d\u0430 \u043f\u0435\u0440\u0435\u043a\u0440\u0435\u0441\u0442\u043a\u0435")
		label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		sizer_2.Add(label_2, 0, wx.ALIGN_CENTER, 0)
		label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044c\u0442\u0435\u0441\u044c")
		label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		sizer_2.Add(label_3, 0, wx.ALL, 5)
		label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0418\u043c\u044f")
		label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER, 0)
		grid_sizer_1.Add(self.inpt_name, 0, wx.ALIGN_CENTER, 0)
		inpt_familia1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f")
		inpt_familia1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		grid_sizer_1.Add(inpt_familia1, 0, wx.ALIGN_CENTER, 0)
		grid_sizer_1.Add(self.inpt_familia, 0, wx.ALIGN_CENTER, 0)
		label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u0413\u0440\u0443\u043f\u043f\u0430")
		label_5.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER, 0)
		grid_sizer_1.Add(self.inpt_group, 0, wx.ALIGN_CENTER, 0)
		label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, u"\u2116 \u0417\u0430\u0447\u0435\u0442\u043d\u043e\u0439 \u043a\u043d\u0438\u0436\u043a\u0438")
		label_6.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		grid_sizer_1.Add(label_6, 0, wx.ALIGN_CENTER, 0)
		grid_sizer_1.Add(self.inpt_zachetka, 0, wx.ALIGN_CENTER, 0)
		sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		grid_sizer_2.Add(self.btn_settings, 0, wx.ALIGN_BOTTOM, 0)
		grid_sizer_2.Add(self.btn_next, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)
		sizer_2.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		self.panel_1.SetSizer(sizer_2)
		sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade

	def empty_pole(self):

		dlg = wx.MessageDialog(self, 'Не все поля заполнены. Заполните все поля перед продолжением', 'Ошибка', wx.OK)
		val = dlg.ShowModal()
		if val == wx.ID_OK:
			dlg.Destroy()

	def go_page2(self, event):



		name = self.inpt_name.GetValue()
		name = name.replace(' ', '')

		familia = self.inpt_familia.GetValue()
		if len(familia) == 0:
			self.empty_pole()
			return

		group = self.inpt_group.GetValue()
		if len(group) == 0:
			self.empty_pole()
			return
		zach_number = self.inpt_zachetka.GetValue()
		zach_number = zach_number.replace(' ', '')
		if len(zach_number) == 0:
			self.empty_pole()
			return

		fio = str(familia).lower() + ' ' + str(name).lower()
		new_session = Session()

		if new_session.query(exists().where(Student.fname == fio).
							where(Student.group == group).where(Student.zach_number == zach_number)).scalar():
			print("ЗАГРУЖАЮ ВАШЕ ЗАДАНИЕ")
		else:
			print("пора занести вас в базу и придумать для вас задание")
			student = Student(fname=fio, group=group, zach_number=zach_number)
			new_session.add(student)
			new_session.commit()


		SecondPage.SecondPage.OnInit(SecondPage)
		self.Destroy()




	# todo Перенести весь функционал из main.py
	# todo Подключить логирование
	# todo Настроить относительные пути к ресурсам
	# todo настроить размеры окна


	def setup(self):
		pass


class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None, wx.ID_ANY, "")
		self.frame.Center()
		self.frame.Show()
		return True



if __name__ == "__main__":
	app = MyApp(0)
	app.MainLoop()
