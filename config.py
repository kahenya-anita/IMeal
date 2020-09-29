import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abuga:password@localhost/imeal'
    #heroku database below
    SQLALCHEMY_DATABASE_URI ='postgres://xdjubzsbiwlagr:77a57069ee08f8d45f109a8c1a123436ba9739abdc7cb2279e7e81546c99bb18@ec2-34-233-43-35.compute-1.amazonaws.com:5432/d7mhdn9uq07bgv'
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
