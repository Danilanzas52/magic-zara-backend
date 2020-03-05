# magic-zara-backend
Backend for the zara app.
REST API with Flask

## Run
``` bash
python3 src/main.py
```
Go to [http://127.0.0.1:5000/?category=coat](http://127.0.0.1:5000/?category=coat), for example

## Requirements
- Flask python library
- MongoDB
  - Text index required for keywords search: [see this](https://docs.mongodb.com/manual/core/index-text/)

## Endpoints
- `/`: Get all stored products
  - _category_ (query parameter)
- `/<id>`: Get concrete product
- `/search`: Get products by keywords
 - keywords
