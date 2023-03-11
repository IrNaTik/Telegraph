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

    user_id = await db_provider.user.get_user_id('500000')
    print(user_id , datetime.now() - start_time)
    
    # async with AsyncSession(engine) as session:
    #         for i in range(70001, 1000000):
          
    #             statement = text(f"""INSERT INTO user(login, password) VALUES('{i}', '{i}')""")
    #             await session.execute(statement)
            
    #         
    #         await session.commit()
    
        


asyncio.run(async_main())


