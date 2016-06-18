class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my secrect'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./posts.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    # absolutely sure!
    DEBUG = False
