import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abuga:password@localhost/imeal'
    #heroku database below
    SQLALCHEMY_DATABASE_URI ='postgres://ylazfenhkwzwpv:a38e1a7e4a7cd82e42e531b8e90b22240cc1345462add3cf7762806399289dfb@ec2-52-20-160-44.compute-1.amazonaws.com:5432/dt204hkjoqd90'
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
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


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
