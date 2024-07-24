from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SiteData(Base):
    __tablename__ = 'sitedata'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_code = Column(String, nullable=False)
    stream_flow_unit = Column(String)
    stream_flow_value = Column(Numeric)
    guage_height_unit = Column(String)
    guage_height_value = Column(Numeric)
    timestamp = Column(String)