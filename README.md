# Marvel-Stories

Marvel-Stories is a service for collecting information about stories from your favorite Marvel® character.

## Dependencies

(optional) Setup virtual env.
```bash
python3 -m venv ./env && source env/bin/activate
```

Use pip to install Marvel-Stories dependencies.
```bash
python3 -m pip install -r requirements.txt
```

## Running

Marvel-Stories runs on Flask.

```bash
flask run
```

Requests can be made using the URL.

`http://localhost:5000/`

## Testing

You must first export the variables defined in the `.flaskenv` e.g., `export FAVORITE_HERO_NAME=Spider-Man`.

```bash
cat .flaskenv | while read line; do export ${line}; done
```

With the service running as shown above, run the tests.
```bash
pytest -v
```

## Built with
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)