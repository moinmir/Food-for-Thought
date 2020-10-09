class Config:
    GOOGLEMAPS_KEY = "AIzaSyAOhs8UoLOWiqJwDXie6Igf8TJWw-IQkQM"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SECRET_KEY = "7501d06b12422d9792968f951c600b32"

    # app config for email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "officialfoodforthought@gmail.com"
    MAIL_PASSWORD = "food.for.thought"