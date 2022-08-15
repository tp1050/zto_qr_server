import qrcode



class dool_qr(Object):
    def __init__(self,data="DOOL",img=none,path=none):
        qr=qrcode.QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        img=qr.make_image(fill_color='red',back_color='white')
        img.save('myQRcODE.jpg')
