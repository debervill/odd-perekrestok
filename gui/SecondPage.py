import wx
import random
import os


class SeconPageFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SeconPageFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((658, 331))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.panel_1.SetBackgroundColour(self.color)
        self.radio_btn_2 = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Крестообразный")
        self.radio_btn_3 = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Т-образный")
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")

        self.text_ctrl_1.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda)
        self.text_ctrl_2.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda)
        self.radio_btn_2.SetValue(True)

        self.__set_properties()
        self.__do_layout()
        self.set_kat_dor()

    def scale_bitmap(self, bitmap, width, height):
        self.w = width
        self.h = height
        image = wx.Image(bitmap)
        image = image.Scale(self.w, self.h, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def __set_properties(self):
        # begin wxGlade: SeconPageFrame.__set_properties
        self.SetTitle("Расчет цикла светофорного регулирования")

    def __do_layout(self):
        # begin wxGlade: SeconPageFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "sizer_2"), wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(1, 6, 0, 0)
        grid_sizer_3 = wx.GridSizer(0, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(0, 4, 0, 0)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Исходные данные для расчета")
        label_1.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория \n Горизональной улицы")
        grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.katHorizont = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(self.katHorizont, 0, wx.ALIGN_CENTER, 0)

        label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория \n Вертикальной улицы")
        grid_sizer_1.Add(label_9, 0, wx.ALIGN_CENTER, 0)
        self.katVertical = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.katVertical, 0, wx.ALIGN_CENTER, 0)

        label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос \n Горизонтальной улицы")
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER, 0)
        self.kolvoPolosHorizont = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(self.kolvoPolosHorizont, 0, wx.ALIGN_CENTER, 0)

        label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос \n Вертикальной улицы")
        grid_sizer_1.Add(label_13, 0, wx.ALIGN_CENTER, 0)
        self.kolvoPolosVert = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.kolvoPolosVert, 0, wx.ALIGN_CENTER, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Выберите тип пересечения")
        label_18.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_2.Add(label_18, 0, wx.ALL, 9)
        grid_sizer_3.Add(self.radio_btn_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_3.Add(self.radio_btn_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.bitmap_4 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100,100,  wx.BITMAP_TYPE_ANY))
        grid_sizer_3.Add(self.bitmap_4, 0, 0, 0)

        self.bitmap_5 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100, 100, wx.BITMAP_TYPE_ANY))
        grid_sizer_3.Add(self.bitmap_5, 0, 0, 0)
        sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)

        label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Необходимо расчитать:")
        label_15.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_2.Add(label_15, 0, 0, 0)
        label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части \n Горизонтальной улицы")
        grid_sizer_2.Add(label_16, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 0)
        grid_sizer_2.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100, 100, wx.BITMAP_TYPE_ANY))
        bitmap_2.Hide()
        grid_sizer_2.Add(bitmap_2, 0, 0, 0)

        label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части \n Вертикальной улицы")
        grid_sizer_2.Add(label_17, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)

        bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100, 100, wx.BITMAP_TYPE_ANY))
        grid_sizer_2.Add(bitmap_3, 0, 0, 0)
        sizer_2.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()

    def good(self):
        self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/123.jpg"
        self.img4 = self.scale_bitmap(self.img1, 50, 50)
        self.bitmap_2.SetBitmap(wx.Bitmap(self.img1))
        self.bitmap_2.Show()
        self.Refresh()

    def bad(self):
        self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
        self.img3 = self.scale_bitmap(self.img2, 70, 50)
        self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
        self.bitmap_3.Show()
        self.Refresh()

    def set_kat_dor(self):
        self.kolvoPolosVert.SetLabel(str(random.randint(2, 4)))
        self.kolvoPolosHorizont.SetLabel(str(random.randint(2, 4)))
        self.katHorizont.SetLabel(str(random.randint(2, 4)))
        self.katVertical.SetLabel(str(random.randint(2, 4)))

    def proverka_vvoda(self, event):
        self.pr_Vert = int(self.kolvoPolosHorizont.GetLabel()) * 3.75
        self.pr_hor = int(self.kolvoPolosHorizont.GetLabel()) * 3.75

        print(self.pr_hor)
        print(self.pr_Vert)
        if len(self.text_ctrl_1.GetValue()) > 0:
            if str(self.pr_hor) == self.text_ctrl_1.GetValue():
                self.file = open("123", "w").close()
                self.file = open("123", "w")
                self.file.writelines(self.text_ctrl_1.GetValue() + "\n")
                self.file.close()
                print("good")
                self.bitmap_2.Hide()
                self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/123.jpg"
                self.img4 = self.scale_bitmap(self.img1, 50, 50)
                self.bitmap_2.SetBitmap(wx.Bitmap(self.img4))
                self.bitmap_2.Show()
                self.Refresh()
            else:
                print("bad")
                self.bitmap_2.Hide()
                self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
                self.img3 = self.scale_bitmap(self.img2, 70, 50)
                self.bitmap_2.SetBitmap(wx.Bitmap(self.img3))
                self.bitmap_2.Show()
                self.text_ctrl_1.SetValue(str(self.pr_hor))
                self.Refresh()

        if len(self.text_ctrl_2.GetValue()) > 0:
            if str(self.pr_Vert) == self.text_ctrl_2.GetValue() and len(self.text_ctrl_2.GetValue()) > 0:
                print("good")
                self.bitmap_3.Hide()
                self.img1 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/123.jpg"
                self.img4 = self.scale_bitmap(self.img1, 50, 50)
                self.bitmap_3.SetBitmap(wx.Bitmap(self.img4))
                self.bitmap_3.Show()
                self.Refresh()
            else:
                print("Bad")
                self.bitmap_3.Hide()
                self.img2 = "/Users/danamir/PycharmProjects/odd-perekrestok/img/bad.jpg"
                self.img3 = self.scale_bitmap(self.img2, 70, 50)
                self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
                self.bitmap_3.Show()
                self.text_ctrl_2.SetValue(str(self.pr_Vert))
                self.Refresh()

    def proverka_radiobtn(self):
        self.s = 1
        print(self.radio_btn_2.GetValue())
        print(self.radio_btn_3.GetValue())
        if self.radio_btn_2.GetValue() == self.radio_btn_2.GetValue():
            self.error_radio_btn()
            self.s = 0
        return self.s

    def go_page3(self, event):
        from gui import page3
        page3.Page3.OnInit(page3)
        self.Destroy()

class SecondPage(wx.App):
    def OnInit(self):
        self.frame = SeconPageFrame(None, wx.ID_ANY, "")
        self.frame.Show()
        return True

# end of class SecondPage

if __name__ == "__main__":
    SeconPage = SecondPage(0)
    SeconPage.MainLoop()
