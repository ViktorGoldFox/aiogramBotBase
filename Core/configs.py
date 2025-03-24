from pydantic_settings import BaseSettings

from typing import List

#=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶
# Bot_config
class BotSettings(BaseSettings):
    token: str = ""

    logs_path: str = "logs.log"
    version: str = 'v1'
#=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶
#=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶
class db_setting(BaseSettings):
    db_path: str = 'database.db' # Path to database file example: database.db (sqlite3)
    url: str = f'sqlite+aiosqlite:///{db_path}' # Select lib of the db
    echo: bool = True # DataBase logs
    autoflush: bool = False #automatic flush call which occurs
    expire_on_commit: bool = False # ХЗ
#====================

class setting(BaseSettings):
    db: db_setting = db_setting()
    bot: BotSettings = BotSettings()