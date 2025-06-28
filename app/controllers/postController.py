from flask import jsonify, request
from werkzeug.utils import secure_filename
from app.services.postService import PostService
from app.config import Config
import os


class PostController:
    @staticmethod
    def _get_request_data():
        """Helper method to get data from either JSON or form-data"""
        if request.is_json:
            return request.get_json()
        else:
            return request.form

    @staticmethod
    def _handle_file_upload():
        """Helper method to handle file upload"""
        if "image" in request.files:
            file = request.files["image"]
            if file.filename != "" and PostService.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
                return filename
        return None

    @staticmethod
    def get_all_posts():
        posts = PostService.get_all_posts()
        return jsonify([post.to_dict() for post in posts])

    @staticmethod
    def get_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if post:
            return jsonify(post.to_dict())
        return jsonify({"error": "Post not found"}), 404

    @staticmethod
    def create_post():
        data = PostController._get_request_data()

        # Get required fields
        author = data.get("author")
        title = data.get("title")
        content = data.get("content")

        if not all([author, title, content]):
            return jsonify({"error": "Missing required fields"}), 400

        # Handle file upload (only for form-data)
        image_filename = None
        if not request.is_json:
            image_filename = PostController._handle_file_upload()
        else:
            image_filename = data.get("image_filename")  # For JSON requests

        post = PostService.create_post(author, title, content, image_filename)
        return jsonify(post.to_dict()), 201

    @staticmethod
    def update_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if not post:
            return jsonify({"error": "Post not found"}), 404

        data = PostController._get_request_data()

        # Get fields to update
        author = data.get("author")
        title = data.get("title")
        content = data.get("content")

        # Handle file upload (only for form-data)
        image_filename = None
        if not request.is_json:
            image_filename = PostController._handle_file_upload()
        else:
            image_filename = data.get("image_filename")  # For JSON requests

        updated_post = PostService.update_post(
            post_id,
            author=author,
            title=title,
            content=content,
            image_filename=image_filename,
        )

        return jsonify(updated_post.to_dict())

    @staticmethod
    def delete_post(post_id):
        success = PostService.delete_post(post_id)
        if not success:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"message": "Post deleted successfully"}), 200
