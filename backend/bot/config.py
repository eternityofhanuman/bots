import os

class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    MONGODB_URI = os.getenv("MONGODB_URI")
    REDIS_URL = os.getenv("REDIS_URL")
    COINGECKO_API = os.getenv("COINGECKO_API")
    ALCHEMY_API = os.getenv("ALCHEMY_API")
    QUICKNODE_API = os.getenv("QUICKNODE_API")
    AWS_KMS_KEY_ID = os.getenv("AWS_KMS_KEY_ID")
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    SUPPORTED_CURRENCIES = ["USDT", "TRX", "BTC", "BNB", "ETH"]
