from flask import Blueprint, send_from_directory
from app.config import Config
from werkzeug.utils import secure_filename
import os

file_bp = Blueprint("files", __name__, url_prefix="/uploads")


@file_bp.route("/<filename>", methods=["GET"])
def get_static(filename):
    # Безопасное получение имени файла
    safe_filename = secure_filename(filename)

    # Проверка существования файла
    file_path = os.path.join(Config.UPLOAD_FOLDER, safe_filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}, 404

    # Проверка типа файла (дополнительная безопасность)
    if not safe_filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        return {"error": "Forbidden file type"}, 403

    return send_from_directory(Config.UPLOAD_FOLDER, safe_filename)
