# from .user import User
# from .chat import Chat_Instance, Chat_Messages
# from .base import session, current_session

from database.base import metadata, engine
from database.user import User, create_user_photos_table
from database.chat import Chat_Instance, create_chat_messages_table, create_chat_messages_pagination_table