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
# print(Post.__table__.columns)
model_fields = {field: new_post.get(field) for field in Post.__table__.columns.keys()}
model_fields["image_filename"] = "express.png"
post = Post(**model_fields)
print(post.to_dict())

setattr(post, "id", 228)

print(post.to_dict())

# # Как получить список ожидаемых от клиента полей:
# print(Post.get_updatable_fields())

# # Как получить список обязательных для клиента полей:
# print(Post.get_required_fields())
