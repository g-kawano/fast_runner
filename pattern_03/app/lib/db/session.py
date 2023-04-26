import json
import os
from urllib.parse import quote

from app.setting import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ローカルDB接続かどうかの判断
if settings.IS_CONNECTION_LOCAL:
    DB_URL = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:3306/{settings.DB_NAME}"
else:
    db_secrets = json.loads(settings.DB_SECRETS)
    DB_URL = f"mysql+pymysql://{quote(db_secrets['DB_USER'])}:{quote(db_secrets['DB_PASS'])}@{quote(settings.DB_HOST)}:3306/{quote(settings.DB_NAME)}?charset=utf8"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

# セッションのコンテキストマネージャ
class SessionScope:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
