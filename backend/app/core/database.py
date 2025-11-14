from sqlalchemy import create_engine

from app.core.config import settings

# 配置并创建全局数据库引擎 engine ，统一连接池与连接健康检查
engine = create_engine(
    settings.database_url
)