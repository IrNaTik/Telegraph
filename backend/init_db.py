#
# Creating start tables(statis tables as User and Chat_Instance)
#

from database_work import db_provider
import asyncio

async def async_main() -> None:
    await db_provider.create_tables()

    await db_provider.user.create_photos_table('Ignat')

asyncio.run(async_main())
