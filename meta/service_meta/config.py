import os

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", default="SECRET_KEY")

# Путь директории всегда заканчивается на "/"
path = "./"
