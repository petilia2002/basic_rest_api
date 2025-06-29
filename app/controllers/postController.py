from flask import jsonify
from werkzeug.utils import secure_filename
from app.services.postService import PostService
from app.utils.request_parser import parse_request
from app.config import Config
import os


class PostController:
    @staticmethod
    def get_all_posts():
        try:
            posts = PostService.get_all_posts()
            return jsonify([post.to_dict() for post in posts])
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def get_post(post_id):
        try:
            post = PostService.get_post_by_id(post_id)
            if post:
                return jsonify(post.to_dict())
            else:
                return jsonify({"Error": "Post not found"}), 404
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def create_post():
        try:
            req = parse_request()
            post = PostService.create_post(req.body, req.files.get("image"))
            return jsonify(post.to_dict()), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def update_post(post_id):
        try:
            req = parse_request()
            updated_post = PostService.update_post(
                post_id, req.body, req.files.get("image")
            )
            if not updated_post:
                return jsonify({"Error": "Post not found"}), 404
            else:
                return jsonify(updated_post.to_dict()), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    @staticmethod
    def delete_post(post_id):
        try:
            post = PostService.delete_post(post_id)
            if not post:
                return jsonify({"Error": "Post not found"}), 404
            else:
                return jsonify(post.to_dict()), 200
        except Exception as e:
            return jsonify({"Error": "Post not found"}), 500
