from app.db.models import db, Post
from app.services.fileService import FileService


class PostService:
    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def create_post(post, file):

        model_fields = {field: post.get(field) for field in Post.get_updatable_fields()}

        missing_fields = [
            field
            for field in Post.get_required_fields()
            if field not in model_fields or model_fields[field] is None
        ]

        if missing_fields:
            raise Exception(f"Missing required fields: {missing_fields}")

        # Handle file upload (only for form-data)
        image_filename = (
            FileService.save_uploaded_file(file) if file else post.get("image_filename")
        )

        model_fields["image_filename"] = image_filename
        new_post = Post(**model_fields)

        try:
            db.session.add(new_post)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return new_post

    @staticmethod
    def update_post(post_id, new_post, file):
        # Get old post for update
        post = Post.query.get(post_id)
        if not post:
            return None

        missing_fields = [
            field
            for field in Post.get_required_fields()
            if field not in new_post or new_post[field] is None
        ]

        if missing_fields:
            raise Exception(f"Missing required fields: {missing_fields}")
        else:
            for field in Post.get_updatable_fields():
                if field in new_post:
                    setattr(post, field, new_post[field])

        # Handle file upload (only for form-data)
        image_filename = (
            FileService.save_uploaded_file(file)
            if file
            else new_post.get("image_filename")
        )

        # Delete associated image if it exists
        if post.image_filename:
            FileService.delete_file(post.image_filename)
        post.image_filename = image_filename

        try:
            db.session.commit()
            db.session.refresh(post)
        except Exception:
            db.session.rollback()
            raise

        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return None

        # Delete associated image if it exists
        if post.image_filename:
            FileService.delete_file(post.image_filename)

        try:
            db.session.delete(post)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return post
