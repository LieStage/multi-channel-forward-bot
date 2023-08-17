import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","6434837886:AAEcF3PP64wNIdYPhedI8_IYUXvfuYibVcM")
    APP_ID = int(os.environ.get("APP_ID","4682685"))
    API_HASH = os.environ.get("API_HASH","3eba5d471162181b8a3f7f5c0a23c307")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "945284066").split())
    CHANNEL1_ID = os.environ.get("CHANNEL1_ID")
    CHANNEL1_NAME = os.environ.get("CHANNEL1_NAME")
    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")
    CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")
    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")
    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")
    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")
    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")
    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")
    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
