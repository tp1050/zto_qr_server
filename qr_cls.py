import qrcode



class dool_qr:
    def __init__(self,data="DOOL",img=None,path=None):
        qr=qrcode.QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        self.img=qr.make_image(fill_color='red',back_color='white')

    def qr(self):
        self.img.save('myQRcODE.jpg')
        return self.img
