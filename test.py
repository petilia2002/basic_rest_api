from app.db.models import Post
from datetime import datetime

# Получаем все допустимые поля модели
new_post = {
    "author": "ulbi tv",
    "title": "Basic Backend",
    "content": "Flask Python PostgreSQL",
    "created_at": datetime.now(),
    "updated_at": datetime.now(),
}

# print(Post.__table__.columns.keys())
model_fields = {field: new_post.get(field) for field in Post.__table__.columns.keys()}
post = Post(**model_fields)
print(post.to_dict())
