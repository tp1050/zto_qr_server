class Conf(object):
    SECRET_KEY = "22111357"
    UPLOAD_FOLDER='/img'
    instance_relative_config=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST='0.0.0.0'
    PORT=5000
    SERVER_NAME='192.168.2.66:5000'
