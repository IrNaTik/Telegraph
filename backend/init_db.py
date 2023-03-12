#
# Creating start tables(statis tables as User and Chat_Instance)
#

from database_work import db_provider
import asyncio
import random
import string
from datetime import datetime
import time

from database import  engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

start_time = datetime.now()




async def async_main() -> None:
    await db_provider.create_tables()

    
    alphabet = list(string.ascii_lowercase)

    # user_id = await db_provider.user.get_user_id('500000')
    # print(user_id , datetime.now() - start_time)
    
    # async with AsyncSession(engine) as session:
    #         for i in range(70001, 1000000):
          
    #             statement = text(f"""INSERT INTO user(login, password) VALUES('{i}', '{i}')""")
    #             await session.execute(statement)
            
    #         
    #         await session.commit()

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

    a = await db_provider.user.get_by_prefix('Titan')
    print(a,  datetime.now() - start_time)
            
    
    


asyncio.run(async_main())


