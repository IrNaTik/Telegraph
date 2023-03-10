from database_work import db_provider
import asyncio

# 
# Этот файл - просто пример работы с бд
#

# db_provider.add_user('Andrew', 'Drf43sdrf')

# db_provider.add_chat('Ignat', 'Andrew')
# db_provider.add_message('ignat_andrew', 'Andrew', 'Hello, Ignat')




async def async_main() -> None:
    await db_provider.create_tables()

    chat = await db_provider.add_chat('Andrew', 'Ignat')
    print(chat)
    # a = await db_provider.get_user_chats('Andrew')
    # b = await db_provider.get_chat_messages('ignat_andrew')
    # c = await db_provider.add_message('ignat_andrew', 'Andrew', 'Hello, Ignat')
   
    # print(a[0].__dict__)
    # for row in b:
    #     print(row)
    


asyncio.run(async_main())
