class Conf(object):
    SECRET_KEY = "22111357"
    UPLOAD_FOLDER='/img'
    instance_relative_config=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME='127.0.0.1:8700'

 # 
 # import pacparser
 # pacparser.init()
 # pacparser.parse_pac('httppac.pac')
 # pacparser.find_proxy('http://www.google.com', 'www.google.com')
 # pacparser.setmyip("192.168.5.2")
 # pacparser.find_proxy('http://www.google.com', 'www.google.com')
 # pacparser.find_proxy('http://www2.manugarg.com', 'www2.manugarg.com')
 #
 # pacparser.cleanup()
