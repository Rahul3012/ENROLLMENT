import os

class Config(object):
    SECRET_KEY = os.environ.get('secret_key') or b'\xef-}\xa2\xd1\x84,\xee\x84\x05iW\xb9\x85q\r'
    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}