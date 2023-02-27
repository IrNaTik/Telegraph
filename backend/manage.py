from aiohttp import web  


from apps.auth.routes import urlpatterns


def setup_routes(application):
    urlpatterns(application)  

def setup_external_libraries(application: web.Application) -> None:
    # настройки внешних библиотек
    pass

def setup_app(application):
    setup_external_libraries(application)  
    setup_routes(application) 

app = web.Application()

if __name__ == "__main__":  # эта строчка указывает, что данный файл можно запустить как скрипт
    setup_app(app)  # настраиваем приложение
    web.run_app(app)  # запускаем приложение

    handler = app.make_handler(
        debug=debug,
    )

    if debug:
        aiohttp_autoreload.start()



