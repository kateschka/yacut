Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kateschka/yacut
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

- Если у вас Linux/macOS

  ```
  source venv/bin/activate
  ```

- Если у вас windows

  ```
  source venv/scripts/activate
  ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### 5. Инициализация базы данных

```sh
flask db upgrade
```

### 6. Запуск приложения

```sh
flask run
```

Приложение будет доступно по адресу: [http://localhost:5000](http://localhost:5000)

---

## Тестирование

Для запуска тестов используйте команду:

```sh
pytest
```

---

## Дополнительно

- Для заполнения тестовыми данными используйте команды из файла `postman_collection/set_up_data.sh`.
- Документация по API доступна в файле `openapi.yaml`.

---

## Автор - Кузнецова Екатерина.
