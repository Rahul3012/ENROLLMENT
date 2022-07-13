import os

class Config(object):
    SECRET_KEY = os.environ.get('secret_key') or 'test_secret'
    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}