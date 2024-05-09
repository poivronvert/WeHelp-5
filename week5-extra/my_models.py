from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, comment='Name')
    username = Column(String(255), nullable=False, comment='Username')
    password = Column(String(255), nullable=False, comment='Password')
    follower_count = Column(Integer, nullable=False, default=0, comment='Follower Count')
    time = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', comment='Signup Time')
