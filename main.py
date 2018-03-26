# -*- coding: utf-8 -*-
import wx
import wx.xrc
import sqlite3


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


############################################################################# Class MainFramePanel
###########################################################################

class MainFramePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.FULL_REPAINT_ON_RESIZE)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_kaf = wx.StaticText(self, wx.ID_ANY, u"Кафедра «Организация и безопасность движения»",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_kaf.Wrap(-1)
        bSizer1.Add(self.lbl_kaf, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.lbl_NameProg = wx.StaticText(self, wx.ID_ANY, u"Расчёт цикла светофорного регулирования на перекрёстке\n",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_NameProg.Wrap(-1)
        bSizer1.Add(self.lbl_NameProg, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.lbl_predstv = wx.StaticText(self, wx.ID_ANY, u"Предстваьтесь", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_predstv.Wrap(-1)
        bSizer1.Add(self.lbl_predstv, 0, wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.lbl_name = wx.StaticText(self, wx.ID_ANY, u"Имя", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_name.Wrap(-1)
        fgSizer1.Add(self.lbl_name, 0, wx.ALL, 5)

        self.inpt_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_name, 0, wx.ALL, 5)

        self.lbl_familia = wx.StaticText(self, wx.ID_ANY, u"Фамилия", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_familia.Wrap(-1)
        fgSizer1.Add(self.lbl_familia, 0, wx.ALL, 5)

        self.inpt_familia = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_familia, 0, wx.ALL, 5)

        self.lbl_group = wx.StaticText(self, wx.ID_ANY, u"Группа", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_group.Wrap(-1)
        fgSizer1.Add(self.lbl_group, 0, wx.ALL, 5)

        self.inpt_group = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_group, 0, wx.ALL, 5)

        self.lbl_zachetka = wx.StaticText(self, wx.ID_ANY, u"№ Зачётной книжки", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_zachetka.Wrap(-1)
        fgSizer1.Add(self.lbl_zachetka, 0, wx.ALL, 5)

        self.inpt_zachetka = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_zachetka, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.btn_settongs = wx.Button(self, wx.ID_ANY, u"Настройки", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.btn_settongs, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.btn_page2 = wx.Button(self, wx.ID_ANY, u"Далее", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.btn_page2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.btn_page2.Bind(wx.EVT_BUTTON, self.go_page2)

    def on_init(self):
        pass


    def go_page2(self,event):
        text = []
        login = " "
        name = self.inpt_name.GetValue()
        text.append(name)
        login = ''.join(str(name))
        familia = self.inpt_familia.GetValue()
        text.append(familia)

        group = self.inpt_group.GetValue()
        text.append(group)

        zach_numb = str(self.inpt_zachetka.GetValue())

        variant_num = zach_numb[-2:len(zach_numb)]
        from gui import page2

        page2.MyPanel5.run_page(self)
        print(login)




app = wx.App()
frame = MainFrame(None)
panel = MainFramePanel(frame)
frame.Show()
app.MainLoop()
