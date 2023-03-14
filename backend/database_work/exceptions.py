class Error(Exception):
    """Базовый класс для других исключений"""
    pass

class EmptyValue(Error):
    pass

class IncorrectTypes(Error):
    pass