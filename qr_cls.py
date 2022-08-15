import qrcode
import time


class dool_qr:
    def __init__(self,data="DOOL",img=None,path=None):
        qr=qrcode.QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        self.img=qr.make_image(fill_color='red',back_color='white')
        self.file_name=str(time.time_ns())+str(data)+".jpg"


    def qr(self):

        self.img.save(self.file_name)


        return self.file_name
