import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abuga:password@localhost/imeal'
    #heroku database below
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgres://xlqeblclbdsdvz:c8cc1c6e85a20d48e7000db4008b5064c46a776ac4d8a291eb37f965b4eae68a@ec2-54-90-68-208.compute-1.amazonaws.com:5432/d9ihpl90uohoe0'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
