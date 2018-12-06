import wx
import random


class SeconPageFrame(wx.Frame):
	def scale_bitmap(self, bitmap, width, height):
		self.w = width
		self.h = height
		image = wx.Image(bitmap)
		image = image.Scale(self.w, self.h, wx.IMAGE_QUALITY_HIGH)
		result = wx.Bitmap(image)
		return result

	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((800, 600))
		self.radio_btn_2 = wx.RadioButton(self, wx.ID_ANY, u"Крестообразный\n")
		self.radio_btn_3 = wx.RadioButton(self, wx.ID_ANY, u"Т-образный")
		self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)

		self.text_ctrl_1.Bind(wx.EVT_TEXT_ENTER, self.proverka)
		self.text_ctrl_2.Bind(wx.EVT_TEXT_ENTER, self.proverka)


		self.__set_properties()
		self.__do_layout()
		self.set_kat_dor()



	def __set_properties(self):
		self.SetTitle("Расчёт цикла светофорного регулирования")

	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_2 = wx.GridSizer(0, 3, 20, 100)
		grid_sizer_3 = wx.FlexGridSizer(0, 2, 20, 200)
		grid_sizer_1 = wx.GridSizer(0, 4, 0, 0)
		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

		label_6 = wx.StaticText(self, wx.ID_ANY, u"Исходные данные для расчёта:")
		label_6.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		sizer_1.Add(label_6, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

		label_7 = wx.StaticText(self, wx.ID_ANY, u"Категория \n горизонтальной улицы")
		grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER | wx.ALL, 10)

		self.kat_horizont = wx.StaticText(self, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
		grid_sizer_1.Add(self.kat_horizont, 0, wx.ALIGN_CENTER, 0)

		label_9 = wx.StaticText(self, wx.ID_ANY, u"Категория \n вертикальной улицы")
		grid_sizer_1.Add(label_9, 0, wx.ALIGN_CENTER, 0)

		self.kat_vertical = wx.StaticText(self, wx.ID_ANY, "")
		grid_sizer_1.Add(self.kat_vertical, 0, wx.ALIGN_CENTER, 0)

		label10= wx.StaticText(self, wx.ID_ANY, u"Количество полос \n горизонтальной улицы")
		grid_sizer_1.Add(label10, 0, wx.ALIGN_CENTER, 0)

		self.kolvo_polosv_horiz = wx.StaticText(self, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
		grid_sizer_1.Add(self.kolvo_polosv_horiz, 0, wx.ALIGN_CENTER, 0)

		label_13 = wx.StaticText(self, wx.ID_ANY, u"Количество полос \n вертикальной улицы")
		grid_sizer_1.Add(label_13, 0, wx.ALIGN_CENTER, 0)

		self.kolvo_polosv_vert = wx.StaticText(self, wx.ID_ANY, "")
		grid_sizer_1.Add(self.kolvo_polosv_vert, 0, wx.ALIGN_CENTER, 0)

		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		label_18 = wx.StaticText(self, wx.ID_ANY, u"Выберите тип пересечения:")
		label_18.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))

		sizer_1.Add(label_18, 0, wx.ALL, 9)
		grid_sizer_3.Add(self.radio_btn_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		grid_sizer_3.Add(self.radio_btn_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

		img = self.scale_bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/perekr-4.jpg", 150, 150)
		bitmap_4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap())
		bitmap_4.SetBitmap(wx.Bitmap(img))
		grid_sizer_3.Add(bitmap_4, 0, 0, 0)

		img = self.scale_bitmap("/Users/danamir/PycharmProjects/odd-perekrestok/img/perekr-t.jpg", 150, 150)
		bitmap_5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap())
		bitmap_5.SetBitmap(wx.Bitmap(img))
		grid_sizer_3.Add(bitmap_5, 0, 0, 0)

		sizer_1.Add(grid_sizer_3, 1, wx.CENTER, 0)

		label_15 = wx.StaticText(self, wx.ID_ANY, u"Вам необходимо рассчитать:")
		label_15.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		sizer_1.Add(label_15, 0, 0, 0)

		label_16 = wx.StaticText(self, wx.ID_ANY, u"Ширину проезжей части \n горизонтальной улицы")
		grid_sizer_2.Add(label_16, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 0)
		grid_sizer_2.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)

		self.bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.EmptyBitmap(75, 75))
		self.bitmap_2.Hide()
		grid_sizer_2.Add(self.bitmap_2, 0, wx.ALIGN_CENTER, 0)

		label_17 = wx.StaticText(self, wx.ID_ANY, u"Ширину проезжей части \n вертикальной улицы")
		grid_sizer_2.Add(label_17, 0, 0, 0)
		grid_sizer_2.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)

		self.bitmap_3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(75, 75))
		self.bitmap_3.Hide()
		grid_sizer_2.Add(self.bitmap_3, 0, 0, 0)

		sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)


		self.btn_page3 = wx.Button(self, wx.ID_ANY, u"Далее", wx.DefaultPosition, wx.DefaultSize, 0)
		btn_sizer.Add(self.btn_page3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)
		sizer_1.Add(btn_sizer, 1, wx.EXPAND, 0)
		self.btn_page3.Bind(wx.EVT_BUTTON, self.go_page3)
		self.SetSizer(sizer_1)
		self.Layout()

	def good(self):
		self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg"
		self.img4 = self.scale_bitmap(self.img1, 50, 50)
		self.bitmap_2.SetBitmap(wx.Bitmap(self.img1))
		self.bitmap_2.Show()
		self.Refresh()


	def bad(self):
		self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/error.jpg"
		self.img3 = self.scale_bitmap(self.img2, 70, 50)
		self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
		self.bitmap_3.Show()
		self.Refresh()


	def set_kat_dor(self):
		self.kolvo_polosv_vert.SetLabel(str(random.randint(2, 4)))
		self.kolvo_polosv_horiz.SetLabel(str(random.randint(2, 4)))
		self.kat_horizont.SetLabel(str(random.randint(2, 4)))
		self.kat_vertical.SetLabel(str(random.randint(2, 4)))

	def proverka(self, event):
		print(self.text_ctrl_1.GetValue())
		print(self.text_ctrl_2.GetValue())

		self.pr_Vert = int(self.kolvo_polosv_horiz.GetLabel()) * 3.75
		self.pr_hor = int(self.kolvo_polosv_horiz.GetLabel()) * 3.75

		print(self.pr_hor)
		print(self.pr_Vert)

		if str(self.pr_hor) == self.text_ctrl_1.GetValue():
			print("good")
			self.bitmap_2.Hide()
			self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg"
			self.img4 = self.scale_bitmap(self.img1, 50, 50)
			self.bitmap_2.SetBitmap(wx.Bitmap(self.img4))
			self.bitmap_2.Show()
			self.Refresh()
		else:
			print("bad")
			self.bitmap_2.Hide()
			self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/error.jpg"
			self.img3 = self.scale_bitmap(self.img2, 70, 50)
			self.bitmap_2.SetBitmap(wx.Bitmap(self.img3))
			self.bitmap_2.Show()
			self.Refresh()

		if str(self.pr_Vert) == self.text_ctrl_2.GetValue() and len(self.text_ctrl_2.GetValue()) > 0:
			print("good")
			self.bitmap_3.Hide()
			self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/good.jpg"
			self.img4 = self.scale_bitmap(self.img1, 50, 50)
			self.bitmap_3.SetBitmap(wx.Bitmap(self.img4))
			self.bitmap_3.Show()
			self.Refresh()
		else:
			print("Bad")
			self.bitmap_3.Hide()
			self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/error.jpg"
			self.img3 = self.scale_bitmap(self.img2, 70, 50)
			self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
			self.bitmap_3.Show()
			self.Refresh()

	def go_page3(self):
		pass

class SecondPage(wx.App):
	def OnInit(self):
		self.frame = SeconPageFrame(None, wx.ID_ANY, "")
		self.frame.Show()
		return True


if __name__ == "__main__":
	SeconPage = SecondPage(0)
	SeconPage.MainLoop()
