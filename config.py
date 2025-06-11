import os

class Config:
    PRODUCTION = False
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_SSL_STRICT = False
    MAX_CONTENT_LENGTH = 1024 * 1024 * 50
    UPLOAD_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".webp"]