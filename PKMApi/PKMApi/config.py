SECRET_KEY = "django-insecure-g6%&9mu7^h20+7y9ujzw=kl=qiv)p+@@fol+1^xg9^k!g7yw77"

AWS_ACCESS_KEY_ID = 'YCAJEm-2S-mHduWCtZqItQD1G'
AWS_SECRET_ACCESS_KEY = 'YCOrn0-JVO8Ale7lyFdEtKyg9ZPuOR-dkDCZEbzF'
AWS_STORAGE_BUCKET_NAME = 'userstoragepkm'
AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
AWS_S3_REGION_NAME = 'ru-central1'

DEFAULT_FILE_STORAGE = 'yandex_s3_storage.ClientImgStorage'
MEDIA_URL = 'https://userstoragepkm.storage.yandexcloud.net/media/'


NAME = 'main_db'
USER = 'postgres'
PASSWORD = '12345678'
HOST = 'localhost'
PORT = '5432'
