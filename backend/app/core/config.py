from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# 定义全局配置对象 settings ，集中管理应用、服务器、数据库、AI、认证安全、CORS、集成、监控、日志、上传等配置项
class Settings(BaseSettings):
