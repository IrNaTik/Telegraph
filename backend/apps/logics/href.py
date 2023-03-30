def create_href(first_id, second_id, start: int) -> str:
    return f'http:///localhost:8000/message?first_id={first_id}&second_id={second_id}&start={start}'
