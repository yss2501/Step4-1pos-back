from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# .env ファイルの読み込み
load_dotenv()

# .env から接続文字列を取得
DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("環境変数 DATABASE_URL が設定されていません。")

# SQLAlchemy エンジン作成
engine = create_engine(DB_URL, echo=True)

# セッション作成
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# ベースクラス
Base = declarative_base()
