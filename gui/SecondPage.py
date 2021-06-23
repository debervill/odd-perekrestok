import wx
import random
import controller
import os
import logging
import platform


class SecondPageFrame(wx.Frame):
    #Логирование
    #срез 18
    def __init__(self, *args, **kwds):

        logging.basicConfig(filename="..\\app.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

        logging.info("second page runing")

        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 800))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)


        

        # self.panel_1.SetBackgroundColour(self.color)
        self.radio_krest = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Крестообразный")
        self.radio_t_obr = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Т-образный")
        self.shir_horiz = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.shir_vert = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.radio_krest.SetValue(True)

        self.shir_horiz.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda)
        self.shir_vert.Bind(wx.EVT_TEXT_ENTER, self.proverka_vvoda)


        self.runPath = os.path.abspath(__file__)
        print(self.runPath)

        if platform.system() == "Windows":
            self.delitel = "\\"
            self.imgPath = self.runPath[:-17] + "img" + self.delitel

            print(self.imgPath)


        self.__set_properties()
        self.__do_layout()
        self.set_kat_dor()

    def scale_bitmap(self, bitmap, width, height):
        self.w = width
        self.h = height
        self.image = wx.Image(bitmap)
        self.image = self.image.Scale(self.w, self.h, wx.IMAGE_QUALITY_HIGH)
        self.result = wx.Bitmap(self.image)
        return self.result

    def __set_properties(self):
        # begin wxGlade: SeconPageFrame.__set_properties
        self.SetTitle("Расчет цикла светофорного регулирования")

        self.color = controller.setBacgroundColor()
        self.SetBackgroundColour(self.color)
        self.btnColor = controller.setBckgroundButtonColor()
        # self.btn2.SetBackgroundColour(self.btnColor)

    def __do_layout(self):
        print(self.runPath)
        print(self.imgPath)
        print(platform.system())

        self.sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, ""), wx.VERTICAL)
        self.grid_sizer_2 = wx.FlexGridSizer(1, 6, 0, 0)
        self.grid_sizer_3 = wx.GridSizer(0, 2, 0, 0)
        self.grid_sizer_1 = wx.GridSizer(0, 4, 0, 0)

        self.label_ish_dan = wx.StaticText(self.panel_1, wx.ID_ANY, u"Исходные данные для расчета")
        self.label_ish_dan.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.sizer_2.Add(self.label_ish_dan, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.label_kat_horiz = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория \n Горизональной улицы")
        self.grid_sizer_1.Add(self.label_kat_horiz, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.katHorizont = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
        self.grid_sizer_1.Add(self.katHorizont, 0, wx.ALIGN_CENTER, 0)

        self.label_kat_vert = wx.StaticText(self.panel_1, wx.ID_ANY, u"Категория \n Вертикальной улицы")
        self.grid_sizer_1.Add(self.label_kat_vert, 0, wx.ALIGN_CENTER, 0)
        self.katVertical = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        self.katVertical = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        self.grid_sizer_1.Add(self.katVertical, 0, wx.ALIGN_CENTER, 0)

        self.label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос \n Горизонтальной улицы")
        self.grid_sizer_1.Add(self.label_11, 0, wx.ALIGN_CENTER, 0)
        self.kolvoPolosHorizont = wx.StaticText(self.panel_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
        self.grid_sizer_1.Add(self.kolvoPolosHorizont, 0, wx.ALIGN_CENTER, 0)

        self.label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Количество полос \n Вертикальной улицы")
        self.grid_sizer_1.Add(self.label_13, 0, wx.ALIGN_CENTER, 0)
        self.kolvoPolosVert = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        self.grid_sizer_1.Add(self.kolvoPolosVert, 0, wx.ALIGN_CENTER, 0)
        self.sizer_2.Add(self.grid_sizer_1, 1, wx.EXPAND, 0)

        self.label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Выберите тип пересечения")
        self.label_18.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.sizer_2.Add(self.label_18, 0, wx.ALL, 9)
        self.grid_sizer_3.Add(self.radio_krest, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.grid_sizer_3.Add(self.radio_t_obr, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)



        self.label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Необходимо расчитать:")
        self.label_15.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.sizer_2.Add(self.label_15, 0, 0, 0)
        self.label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части \n Горизонтальной улицы")
        self.grid_sizer_2.Add(self.label_16, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 0)
        self.grid_sizer_2.Add(self.shir_horiz, 0, wx.ALIGN_CENTER, 0)

        self.bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100, 100, wx.BITMAP_TYPE_ANY))
        self.bitmap_2.Hide()
        self.grid_sizer_2.Add(self.bitmap_2, 0, 0, 0)

        self.label_17 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Ширину проезжей части \n Вертикальной улицы")
        self.grid_sizer_2.Add(self.label_17, 0, 0, 0)
        self.grid_sizer_2.Add(self.shir_vert, 0, wx.ALIGN_CENTER, 0)

        self.bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap(100, 100, wx.BITMAP_TYPE_ANY))
        self.grid_sizer_2.Add(self.bitmap_3, 0, 0, 0)
        self.sizer_2.Add(self.grid_sizer_2, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Далее")
        self.sizer_2.Add(self.button_1, 0, wx.ALIGN_RIGHT, 0)

        self.panel_1.SetSizer(self.sizer_2)
        self.sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(self.sizer_1)
        self.Layout()

    def good(self):
        self.img1 = self.imgPath + "123.jpg"
        self.img4 = self.scale_bitmap(self.img1, 50, 50)
        self.bitmap_2.SetBitmap(wx.Bitmap(self.img1))
        self.bitmap_2.Show()
        self.Refresh()

    def bad(self):
        self.img1 = self.imgPath + "bad.jpg"
        self.img3 = self.scale_bitmap(self.img1, 70, 50)
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
        if len(self.shir_horiz.GetValue()) > 0:
            if str(self.pr_hor) == self.shir_horiz.GetValue():
                self.file = open("123", "w").close()
                self.file = open("123", "w")
                self.file.writelines(self.shir_horiz.GetValue() + "\n")
                self.file.close()
                print("good")
                self.bitmap_2.Hide()
                self.img1 = self.imgPath + "123.jpg"
                self.img4 = self.scale_bitmap(self.img1, 50, 50)
                self.bitmap_2.SetBitmap(wx.Bitmap(self.img4))
                self.bitmap_2.Show()
                self.Refresh()
            else:
                print("bad")
                self.bitmap_2.Hide()
                self.img1 = self.imgPath + "bad.jpg"
                self.img3 = self.scale_bitmap(self.img1, 70, 50)
                self.bitmap_2.SetBitmap(wx.Bitmap(self.img3))
                self.bitmap_2.Show()
                self.shir_horiz.SetValue(str(self.pr_hor))
                self.Refresh()

        if len(self.shir_vert.GetValue()) > 0:
            if str(self.pr_Vert) == self.shir_vert.GetValue() and len(self.shir_vert.GetValue()) > 0:
                print("good")
                self.bitmap_3.Hide()
                self.img1 = self.imgPath + "123.jpg"
                self.img4 = self.scale_bitmap(self.img1, 50, 50)
                self.bitmap_3.SetBitmap(wx.Bitmap(self.img4))
                self.bitmap_3.Show()
                self.Refresh()
            else:
                print("Bad")
                self.bitmap_3.Hide()
                self.img1 = self.imgPath + "bad.jpg"
                self.img3 = self.scale_bitmap(self.img1, 70, 50)
                self.bitmap_3.SetBitmap(wx.Bitmap(self.img3))
                self.bitmap_3.Show()
                self.shir_vert.SetValue(str(self.pr_Vert))
                self.Refresh()

    def proverka_radiobtn(self):
        self.s = 1
        print(self.radio_krest.GetValue())
        print(self.radio_t_obr.GetValue())
        if self.radio_krest.GetValue() == self.radio_krest.GetValue():
            self.error_radio_btn()
            self.s = 0
        return self.s

    def go_page3(self, event):
        from gui import page3
        page3.Page3.OnInit(page3)
        self.Destroy()


class SecondPage(wx.App):
    def OnInit(self):
        self.frame = SecondPageFrame(None, wx.ID_ANY)
        self.frame.Show()
        self.frame.Center()

        return True


if __name__ == "__main__":
    SeconPage = SecondPage(0)
    SeconPage.MainLoop()
