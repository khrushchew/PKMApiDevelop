SECRET_KEY = "django-insecure-g6%&9mu7^h20+7y9ujzw=kl=qiv)p+@@fol+1^xg9^k!g7yw77"

AWS_ACCESS_KEY_ID = 'YCAJE49q2KSztJcfMILYI7Np1'
AWS_SECRET_ACCESS_KEY = 'YCMn_xJF02syxFlpWfpt-aMYaWYNfD3-Np7DyujX'
AWS_STORAGE_BUCKET_NAME = 'userstoragepkm'
AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
AWS_S3_REGION_NAME = 'ru-central1'

DEFAULT_FILE_STORAGE = 'yandex_s3_storage.S3LogStorage'
MEDIA_URL = 'https://userstoragepkm.storage.yandexcloud.net/media/'


NAME = 'main_db'
USER = 'postgres'
PASSWORD = '12345678'
HOST = 'localhost'
PORT = '5432'
