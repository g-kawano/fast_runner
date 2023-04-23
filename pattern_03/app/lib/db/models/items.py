from app.lib.db.session import SessionScope
from sqlalchemy import Column, Integer, String

from . import Base


# Items モデルの定義
class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}


def get_item_by_id(item_id):
    with SessionScope() as session:
        item = session.query(Items).filter(Items.id == item_id).one_or_none()
        return item.to_dict() if item else None
