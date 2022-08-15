import requests
r = requests.post('http://127.0.0.1:5000/echoJSON', json={
  "Id": 78912,
  "Customer": "Jason Sweet",
  "Quantity": 1,
  "Price": 18.00
})
print(f"Status Code: {r.status_code}, Response: {r.json()}")
# import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

def serve_pil_image(pil_img):
    from io import StringIO
    from flask import send_file

    img_io = StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
