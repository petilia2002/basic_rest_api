from app.config import Config
import os
import uuid
from werkzeug.utils import secure_filename
from datetime import datetime


class FileService:
    @staticmethod
    def generate_unique_filename(original_filename):
        """Генерирует уникальное имя файла"""
        ext = original_filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        return secure_filename(unique_filename)

    @staticmethod
    def save_uploaded_file(file):
        """Сохраняет загруженный файл c уникальным именем"""
        if not file or file.filename == "":
            return None

        filename = FileService.generate_unique_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)

        file.save(filepath)
        return filename
