#
# Creating start tables(statis tables as User and Chat_Instance)
#

from database_work import db_provider
import asyncio
import random
import string
from datetime import datetime
import time

from database import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

start_time = datetime.now()


async def async_main() -> None:
    await db_provider.create_tables()
    # await db_provider.chat.add_chat(1,2)
    # for i in range(1000):
    #     await db_provider.chat.add_message(table_name='1_2', sender_username='Ignatioooo', content=f'Text{i}')
    print(await db_provider.chat.get_chat_messages(table_name='1_2', start=0))
    # a = await db_provider.chat.add_chat(user1_id=2, user2_id=1)
    # print(a['chat_name'])

    # alphabet = list(string.ascii_lowercase)

    # user_id = await db_provider.user.get_user_id('500000')
    # print(user_id , datetime.now() - start_time)

    # for i in range(1000):
    #     await db_provider.user.add_user(str(i), str(i))

    # prefix = '9'
    # async with AsyncSession(engine) as session:

    #         statement = text(f"""SELECT * FROM user WHERE login LIKE '{prefix}%' LIMIT 10""")
    #         objects = await session.execute(statement)

    #         arr = []
    #         for row in objects:

    #             arr.append(row)

    #         print(arr)
    #         print(arr[0].login)
    #         print(objects , datetime.now() - start_time)

    # a = await db_provider.user.get_by_prefix('Titan')
    # print(a,  datetime.now() - start_time)

    # c = await db_provider.chat.get_chat_messages('', 1000)

    # c = await db_provider.user.add_user('Igantio', 'fjfvfvgfd')
    # c = await db_provider.user.add_photo('kmlfksljdfdnl', 'fjdshfsjdhfdsjhfdkjs')
    # print(c, datetime.now() - start_time)

    # for  i in range(15):
    #     c = await db_provider.chat.add_message('999_99', 'Titan', f'Hello world {i}')
    #     print(c)

    # c = await db_provider.chat.get_chat_messages('999_99', 20)
    # print(c)

    # names = ['Ignatioooo', 'Andrewwwww', 'Grigoriiiii', 'Igorrrrrr', 'Ivannnnnn']
    # for el in names:
    #     a = await db_provider.user.add_user(el, el, el)
    #     print(a)
    # print('Good')


asyncio.run(async_main())
