import wx

def scale_bitmap(bitmap):
    dw, dh = wx.DisplaySize()
    image = bitmap.ConvertToImage()
    image = image.Scale(dw, dh, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class Panel(wx.Panel):
    def __init__(self, parent, path):
        super(Panel, self).__init__(parent, -1)
        bitmap = wx.Bitmap(path)
        bitmap = scale_bitmap(bitmap)
        control = wx.StaticBitmap(self, -1, bitmap)
        control.SetPosition((0, 0))

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Scaled Image')
    panel = Panel(frame, 'input.jpg')
    frame.Show()
    app.MainLoop()
