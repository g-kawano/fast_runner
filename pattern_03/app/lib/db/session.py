import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 環境変数から設定値を取得
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]

IS_CONNECTION_LOCAL = os.environ.get("IS_CONNECTION_LOCAL", False)

# ローカルDB接続かどうかの判断
if IS_CONNECTION_LOCAL:

    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
else:
    DB_URL = "your_remote_db_url_here"

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
