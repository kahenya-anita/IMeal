import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abuga:password@localhost/imeal'
    #heroku database below
    #SQLALCHEMY_DATABASE_URI ='postgres+psycopg2://lfgiafilewplkg:652bbbf039b88462ef1ce2fc405a8a4a434e53c197f30b192ca0ff51e636234b@ec2-3-210-255-177.compute-1.amazonaws.com:5432/d8jd2q7ohb0q7k'

    SQLALCHEMY_TRACK_MODIFICATIONS = True


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
