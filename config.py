import os

class Config(object):
    SECRET_KY = os.environ.get('secret_key') or 'test_secret'
    MONGODB_SETTINGS = {'db':'UTA_Enrollment', 
        'host': 'mongodb://localhost:27017/UTA_Enrollment'
    }