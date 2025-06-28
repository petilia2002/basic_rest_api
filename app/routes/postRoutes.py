from flask import Blueprint
from app.controllers.postController import PostController

post_bp = Blueprint("posts", __name__)


@post_bp.route("/posts", methods=["GET"])
def get_posts():
    return PostController.get_all_posts()


@post_bp.route("/posts", methods=["POST"])
def create_post():
    return PostController.create_post()


@post_bp.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    return PostController.get_post(post_id)


@post_bp.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    return PostController.update_post(post_id)


@post_bp.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    return PostController.delete_post(post_id)
