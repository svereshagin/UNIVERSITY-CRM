Для того чтобы сделать запрос к API второго сервиса из первого сервиса на FastAPI, вы можете использовать библиотеку `httpx`. Это асинхронный HTTP-клиент, который позволяет отправлять запросы к другим сервисам. Вот пошаговая инструкция, как это сделать:

### Шаг 1: Установка httpx

Сначала установите библиотеку `httpx`, если она еще не установлена:
```bash
pip install httpx
```

### Шаг 2: Настройка первого сервиса

В первом сервисе создайте функцию, которая будет отправлять запрос к API второго сервиса. Вот пример:

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

SECOND_SERVICE_URL = "http://localhost:8001"  # URL второго сервиса

@app.get("/get-data-from-second-service/")
async def get_data_from_second_service():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SECOND_SERVICE_URL}/data-endpoint/")
        
        # Проверка статуса ответа
        if response.status_code == 200:
            return response.json()  # Возвращаем данные от второго сервиса
        else:
            return {"error": "Failed to fetch data from second service"}
```

### Шаг 3: Настройка второго сервиса

Во втором сервисе создайте конечную точку, к которой будет отправляться запрос. Например:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/data-endpoint/")
async def data_endpoint():
    return {"message": "Hello from second service!"}
```

### Шаг 4: Запуск сервисов

Запустите оба сервиса в разных терминалах:

Для первого сервиса:
```bash
uvicorn first_service:app --host 127.0.0.1 --port 8000 --reload
```

Для второго сервиса:
```bash
uvicorn second_service:app --host 127.0.0.1 --port 8001 --reload
```

### Шаг 5: Тестирование

Теперь вы можете протестировать взаимодействие между сервисами. Откройте браузер или используйте инструмент, такой как Postman или curl, и перейдите по следующему адресу для первого сервиса:
```
http://127.0.0.1:8000/get-data-from-second-service/
```

Вы должны получить ответ от второго сервиса:
```json
{"message": "Hello from second service!"}
```

### Заключение

Таким образом, вы можете легко делать запросы к API другого сервиса на FastAPI, используя библиотеку `httpx`. Это позволяет вашим сервисам взаимодействовать друг с другом и обмениваться данными. 😊