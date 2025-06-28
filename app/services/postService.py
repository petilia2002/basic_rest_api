from datetime import datetime
from app.db.models import db, Post
from app.config import Config
import os


class PostService:
    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def create_post(author, title, content, image_filename=None):
        new_post = Post(
            author=author, title=title, content=content, image_filename=image_filename
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update_post(
        post_id, author=None, title=None, content=None, image_filename=None
    ):
        post = Post.query.get(post_id)
        if not post:
            return None

        if author is not None:
            post.author = author
        if title is not None:
            post.title = title
        if content is not None:
            post.content = content
        if image_filename is not None:
            # Delete old image if it exists
            if post.image_filename:
                old_image_path = os.path.join(Config.UPLOAD_FOLDER, post.image_filename)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            post.image_filename = image_filename

        db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return False

        # Delete associated image if it exists
        if post.image_filename:
            image_path = os.path.join(Config.UPLOAD_FOLDER, post.image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)

        db.session.delete(post)
        db.session.commit()
        return True

    @staticmethod
    def allowed_file(filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
        )
