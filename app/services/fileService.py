from app.config import Config
import os
import uuid
from werkzeug.utils import secure_filename


class FileService:
    @staticmethod
    def _generate_unique_filename(original_filename):
        """Генерирует уникальное имя файла"""
        ext = original_filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        return secure_filename(unique_filename)

    @staticmethod
    def save_uploaded_file(file):
        """Сохраняет загруженный файл c уникальным именем"""
        if not file or not file.filename:
            return None

        if not FileService.allowed_file(file.filename):
            return None

        try:
            filename = FileService._generate_unique_filename(file.filename)
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)

            file.save(filepath)
            return filename

        except Exception as e:
            print(e)

    @staticmethod
    def delete_file(filename):
        """Удаляет файл c уникальным именем"""
        try:
            image_path = os.path.join(Config.UPLOAD_FOLDER, filename)
            if os.path.exists(image_path):
                os.remove(image_path)
        except Exception as e:
            print(e)

    @staticmethod
    def allowed_file(filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
        )
