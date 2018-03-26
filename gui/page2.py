import wx


class MyFrame4(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)
        self.Maximize(True)

    def __del__(self):
        pass



class MyPanel5(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.FULLSCREEN_NOBORDER)
        self.Bind(wx.EVT_PAINT, self.onPaint)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.imgMaxSize = 200

        self.lbl_zag_page2 = wx.StaticText(self, wx.ID_ANY, u"Схема перекрёстка и  транаспортных потоков на нём",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_zag_page2.Wrap(-1)
        bSizer2.Add(self.lbl_zag_page2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(3, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.lbl_shema = wx.StaticText(self, wx.ID_ANY, u" Схема перекрёстка", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_shema.Wrap(-1)
        fgSizer2.Add(self.lbl_shema, 0, wx.ALL, 5)

        self.lbl_trpotok = wx.StaticText(self, wx.ID_ANY, u"Картограмма транаспортных потоков", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_trpotok.Wrap(-1)
        fgSizer2.Add(self.lbl_trpotok, 0, wx.ALL, 5)

        self.shema_perekr = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"src/shema_01.jpg", wx.BITMAP_TYPE_ANY))

        fgSizer2.Add(self.shema_perekr, 1, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.kartogramma = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"src/kartogramma_perekrestka.gif", wx.BITMAP_TYPE_ANY))

        fgSizer2.Add(self.kartogramma, 1, wx.ALIGN_RIGHT | wx.EXPAND, 5)

        bSizer2.Add(fgSizer2, 1, wx.EXPAND, 5)

        self.btn_page3 = wx.Button(self, wx.ID_ANY, u"Далее", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_page3, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        # Connect Events
        self.btn_page3.Bind(wx.EVT_BUTTON, self.go_page3)

    def onPaint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        x, y = self.GetSize()
        newx =200
        newy=200
        x = newx
        y = newy
        #shema_perekr = self.shema_perekr.Scale()

    # Virtual event handlers, overide them in your derived class
    def go_page3(self, event):
        event.Skip()

    def run_page(self):
        app = wx.App()
        frame = MyFrame4(None)
        panel = MyPanel5(frame)
        frame.Show()
        app.MainLoop()