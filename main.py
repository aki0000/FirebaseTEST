import firebase_admin
from firebase_admin import credentials, messaging

import cloud_messaging

cred = credentials.Certificate("jsonファイルを指定")
default_app = firebase_admin.initialize_app(cred)

token = 'トークンを指定'

messaging = cloud_messaging.cloud_messaging()

messaging.sendToToken(token=token, title='クラス', body='ムズい')

messaging.sendToTopic(topic='29287611', title='TOPIC', body='ムズい')
