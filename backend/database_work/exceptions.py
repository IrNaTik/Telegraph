class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class EmptyValue(Error):
    pass


class IncorrectTypes(Error):
    def __init__(self, error_message) -> None:
        super().__init__()
        self.error_message = error_message


class IncorrectFormat(Error):
    def __init__(self, error_message) -> None:
        super().__init__()
        self.error_message = error_message
