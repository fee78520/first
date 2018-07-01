import os
import MySQLdb

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'a hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <785207019@qq.com>'
    FLASKY_MAIL_SENDER = 'Flasky Admin <17853530715@163.com>'
    FLASKY_ADMIN = '17853530715@163.com'
    #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '17853530715@163.com'
    MAIL_PASSWORD = '785207019li'
    # MAIL_PASSWORD = 'efdvjnmdpfkxbbfc'
    UPLOAD__FOLDER = os.getcwd() + '/app/static/image/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 15
    FLASKY_COMMENTS_PER_PAGE = 20
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    # MAIL_PASSWORD = 'slcwcyguqlfpbffe'

    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/flask_blog'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/flask_blog_test'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/flask_blog_data'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}