
convert epub to plain text

# cli

```
pipenv run python3 main.py alice-in-wonderland.epub
```

# http service

```
uvicorn main:app --reload
```

```
curl -X POST -F "file=@alice-in-wonderland.epub" http://localhost:8000/upload
```