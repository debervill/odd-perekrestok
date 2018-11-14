import wx

class SeconPageFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SeconPageFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((752, 617))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.checkbox_shir_dor1 = wx.CheckBox(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.checkbox_shir_dor2 = wx.CheckBox(self.panel_1, wx.ID_ANY, "")
        self.checkbox_2 = wx.CheckBox(self.panel_1, wx.ID_ANY, "")
        self.bitmap_button_1 = wx.BitmapButton(self.panel_1, wx.ID_ANY, wx.NullBitmap)
        self.checkbox_3 = wx.CheckBox(self.panel_1, wx.ID_ANY, "")
        self.bitmap_button_3 = wx.BitmapButton(self.panel_1, wx.ID_ANY, wx.NullBitmap)
        self.bitmap_button_2 = wx.BitmapButton(self.panel_1, wx.ID_ANY, wx.NullBitmap)
        self.btn_next = wx.Button(self.panel_1, wx.ID_ANY, u"\u0414\u0430\u043b\u0435\u0435")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.raschet_shirinu_dor1, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT_ENTER, self.raschet_shirinu_dor1, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT, self.raschet_shirini_dor2, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT_ENTER, self.raschet_shirini_dor2, self.text_ctrl_2)
        self.Bind(wx.EVT_BUTTON, self.go_next_page, self.btn_next)

    # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SeconPageFrame.__set_properties
        self.SetTitle("frame")
        self.checkbox_shir_dor1.Enable(False)
        self.checkbox_shir_dor1.Hide()
        self.text_ctrl_2.SetMinSize((250, 33))
        self.checkbox_shir_dor2.Enable(False)
        self.checkbox_shir_dor2.Hide()

    # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SeconPageFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.GridSizer(0, 4, 0, 0)
        grid_sizer_2 = wx.GridSizer(0, 3, 0, 0)
        grid_sizer_1 = wx.GridSizer(2, 4, 0, 0)
        lbl_name = wx.StaticText(self.panel_1, wx.ID_ANY,
                                 u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 "
                                 u"\u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f "
                                 u"\u0440\u0430\u0441\u0447\u0435\u0442\u0430:\n",
                                 style=wx.ST_ELLIPSIZE_MIDDLE)
        lbl_name.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        sizer_3.Add(lbl_name, 0, wx.ALIGN_CENTER, 0)
        lbl_doroga1_header = wx.StaticText(self.panel_1, wx.ID_ANY,
                                           u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f "
                                           u"\n\u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c"
                                           u"\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u044b")
        grid_sizer_1.Add(lbl_doroga1_header, 0, wx.FIXED_MINSIZE | wx.TOP, 0)
        kat_1_dorogi = wx.StaticText(self.panel_1, wx.ID_ANY, "kat_1_dorogi")
        grid_sizer_1.Add(kat_1_dorogi, 0, wx.FIXED_MINSIZE | wx.TOP, 0)
        lbl_kat_dor2 = wx.StaticText(self.panel_1, wx.ID_ANY,
                                     u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f "
                                     u"\n\u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 "
                                     u"\u0443\u043b\u0438\u0446\u044b")
        grid_sizer_1.Add(lbl_kat_dor2, 0, wx.EXPAND | wx.TOP, 0)
        kat_dor2 = wx.StaticText(self.panel_1, wx.ID_ANY, "kat_dor2\n")
        grid_sizer_1.Add(kat_dor2, 0, wx.EXPAND | wx.TOP, 0)
        lbl_kolvo_polos_dor1 = wx.StaticText(self.panel_1, wx.ID_ANY,
                                             u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u043e\u0441 \n\u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u044b")
        grid_sizer_1.Add(lbl_kolvo_polos_dor1, 0, wx.TOP, 0)
        kolvo_polos_dor1 = wx.StaticText(self.panel_1, wx.ID_ANY, "kolvo_polos_dor1")
        grid_sizer_1.Add(kolvo_polos_dor1, 0, wx.FIXED_MINSIZE | wx.TOP, 0)
        lbl_kolvo_polos_dor2 = wx.StaticText(self.panel_1, wx.ID_ANY,
                                             u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e "
                                             u"\u043f\u043e\u043b\u043e\u0441\n\u0412\u0435\u0440\u0442\u0438\u043a"
                                             u"\u0430\u043b\u044c\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u044b")
        lbl_kolvo_polos_dor2.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ".SF NS Text"))
        grid_sizer_1.Add(lbl_kolvo_polos_dor2, 0, wx.EXPAND | wx.TOP, 0)
        kolvo_polos_dor2 = wx.StaticText(self.panel_1, wx.ID_ANY, "kolvo_polos_dor2")
        grid_sizer_1.Add(kolvo_polos_dor2, 0, wx.EXPAND | wx.TOP, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        lbl_raschet = wx.StaticText(self.panel_1, wx.ID_ANY,
                                    u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c:\n")
        sizer_3.Add(lbl_raschet, 0, wx.EXPAND | wx.TOP, 0)
        lbl_rasch_dor1 = wx.StaticText(self.panel_1, wx.ID_ANY,
                                       u"\u0428\u0438\u0440\u0438\u043d\u0443 "
                                       u"\u043f\u0440\u043e\u0435\u0437\u0436\u0435\u0439 "
                                       u"\u0447\u0430\u0441\u0442\u0438\n\u0413\u043e\u0440\u0438\u0437\u043e\u043d"
                                       u"\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u044b")
        grid_sizer_2.Add(lbl_rasch_dor1, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER | wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.checkbox_shir_dor1, 0, wx.EXPAND, 0)
        lbl_shiria_dor2 = wx.StaticText(self.panel_1, wx.ID_ANY,
                                        u"\u0428\u0438\u0440\u0438\u043d\u0443 "
                                        u"\u043f\u0440\u043e\u0435\u0436\u0435\u0439 "
                                        u"\u0447\u0430\u0441\u0442\u0438\n\u0412\u0435\u0440\u0442\u0438\u043a\u0430"
                                        u"\u043b\u044c\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u044b")
        grid_sizer_2.Add(lbl_shiria_dor2, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER | wx.FIXED_MINSIZE, 0)
        grid_sizer_2.Add(self.checkbox_shir_dor2, 0, wx.EXPAND, 0)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        lbl_type_prekr = wx.StaticText(self.panel_1, wx.ID_ANY,
                                       u"\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f "
                                       u"\n\u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u044f\n")
        grid_sizer_3.Add(lbl_type_prekr, 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add(self.checkbox_2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_3.Add(self.checkbox_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add(self.bitmap_button_3, 0, 0, 0)
        sizer_3.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizer_3.Add(self.bitmap_button_2, 0, 0, 0)
        sizer_3.Add(self.btn_next, 0, wx.ALIGN_RIGHT, 0)
        self.panel_1.SetSizer(sizer_3)
        sizer_2.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()

    # end wxGlade

    def raschet_shirinu_dor1(self, event):  # wxGlade: SeconPageFrame.<event_handler>
        print("Event handler 'raschet_shirinu_dor1' not implemented!")
        event.Skip()

    def raschet_shirini_dor2(self, event):  # wxGlade: SeconPageFrame.<event_handler>
        print("Event handler 'raschet_shirini_dor2' not implemented!")
        event.Skip()

    def go_next_page(self, event):  # wxGlade: SeconPageFrame.<event_handler>
        print("Event handler 'go_next_page' not implemented!")
        event.Skip()


# end of class SeconPageFrame

class SecondPage(wx.App):
    def OnInit(self):
        self.frame = SeconPageFrame(None, wx.ID_ANY, "")
        self.frame.Show()
        return True


# end of class SecondPage

if __name__ == "__main__":
    SeconPage = SecondPage(0)
    SeconPage.MainLoop()
