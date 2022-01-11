## Hello fast-api

Doing some fast-api testing.

### Launch the app (bash)
```bash
uvicorn app.main:app
```

### Hit the API
```python
>>> import requests
>>> resp = requests.get("http://127.0.0.1:8000")
>>> resp.json()
```

### Hit the items resource
```python
>>> import requests
>>> resp = requests.get("http://127.0.0.1:8000/items/2?q=2")
>>> resp.json()
{'item_id': 2, 'q': '2'}
```

### Build and run Docker container
```bash
docker build . -t fastapi-example
docker run -dp 8000:8000 fastapi-example
```
