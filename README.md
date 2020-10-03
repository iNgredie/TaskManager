- Сервис написан на python3 с использованием любого веб-фреймворка (Django)
- Сервис хранит данные в реляционной базе данных (postgresql)
- Сервис предоставляет интерфейс в виде JSON API, это единственный способ общения клиента с сервисом
- Авторизация в апи происходит с помощью токена (переданного в заголовке Authorization)

------------------------

Регистрация пользователя post запросом на /api/auth/users/

```
{
  "username": "Name",
  "password": "Password"
}
```

------------------

Получение токена post запрос на /api/token/

```
{
  "username": "Name",
  "password": "Password"
}
```

И в ответ

```
{
    "token": "df89e4cc5127d022229ea50fd41be0fbb7ba791d"
}

```

Задачи можно посмотреть /api/task/
 -------------
 
Для запуска в каталоге с файлами

```
docker-compose up

```
