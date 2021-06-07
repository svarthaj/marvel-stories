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

## Env variables

For now, the `.flaskenv` file contains bot API keys (public and private). This is not ideal, but for practical purposes I left it that way.

## Running

Marvel-Stories runs on Flask.

```bash
flask run
```

Requests can be made using the URL.

`http://localhost:5000/`

## Testing

You must first export the variables defined in the `.flaskenv` e.g., `export PUBLIC_API_KEY=1234`.

```bash
cat .flaskenv | while read line; do export ${line}; done
```

With the service running as shown above, run the tests.
```bash
pytest -v
```

## Docker

Marvel-stories is dockerized and you can run it two ways:

### Default

Make sure you have Docker installed in your machine then build the image with

```bash
docker build -t marvel-stories .
```

And then run the service with

```bash
docker run -dp 5000:5000 marvel-stories 
```

### Docker-compose

Make sure you installed `docker-compose` in your machine and then simply run

```bash
docker-compose up
```

## Built with
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Docker](https://www.docker.com)