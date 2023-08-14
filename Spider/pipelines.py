from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (create_engine, sessionmaker)

from Spider.models import *

Base = declarative_base()


class SQLitePipeline:
    def __init__(self):
        self.engine = create_engine('sqlite:///kl.db')
        self.Session = sessionmaker(bind=self.engine)

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

    def open_spider(self, spider):
        self.base = Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def process_spider(self, item, spider):
        return
