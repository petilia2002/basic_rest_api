from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UpdatableMixin:
    __updatable_fields__ = []  # переопределяется в дочерних классах

    @classmethod
    def get_updatable_fields(cls):
        return cls.__updatable_fields__

    @classmethod
    def get_required_fields(cls):
        return [
            col.name
            for col in cls.__table__.columns
            if not col.nullable and not col.primary_key
        ]


class Post(db.Model, UpdatableMixin):
    __tablename__ = "posts"
    __updatable_fields__ = ["author", "title", "content"]

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "image_filename": self.image_filename,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
