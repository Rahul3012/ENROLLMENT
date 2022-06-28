import os

class Config(object):
    SECRET_KY = os.environ.get('secret_key') or 'test_secret'