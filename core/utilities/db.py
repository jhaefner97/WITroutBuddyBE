from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.utilities.utils import DatabaseConfig

cxn_str = f'postgresql+psycopg2://{DatabaseConfig.db_user.value}:{DatabaseConfig.db_password.value}@{DatabaseConfig.db_host.value}:{DatabaseConfig.db_port.value}/{DatabaseConfig.db_name.value}'
engine = create_engine(cxn_str)

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()