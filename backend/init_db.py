from database_work import db_provider

# 
# Этот файл - просто пример работы с бд
#

# db_provider.add_user('Andrew', 'Drf43sdrf')

# db_provider.add_chat('Ignat', 'Andrew')
# db_provider.add_message('ignat_andrew', 'Andrew', 'Hello, Ignat')

a = db_provider.get_user_chats('Ignat')
b = db_provider.get_chat_messages('ignat_andrew')
print(a[0].__dict__)
for row in b:
    print(row)

