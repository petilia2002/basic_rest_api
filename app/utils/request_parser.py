from flask import request
from werkzeug.datastructures import ImmutableMultiDict


def parse_request():
    """Универсальный парсер запросов"""
    # Определяем тип контента
    content_type = request.content_type or ""

    # Инициализируем объект для данных
    request_data = {"params": request.args, "body": {}, "files": ImmutableMultiDict()}

    # Парсим JSON
    if "application/json" in content_type:
        try:
            request_data["body"] = request.get_json() or {}
        except:
            request_data["body"] = {}

    # Парсим form-data и x-www-form-urlencoded
    elif (
        "multipart/form-data" in content_type
        or "application/x-www-form-urlencoded" in content_type
    ):
        request_data["body"] = request.form
        request_data["files"] = request.files

    # Парсим query-параметры (для всех типов запросов)
    request_data["params"] = request.args

    return type("RequestObject", (), request_data)
