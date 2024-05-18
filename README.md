### Description


### This project was build using these tools:
| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [pip](https://pypi.org/project/pip/)                                        | "Package installer for Python"                          |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement" |
| [uvicorn](https://www.uvicorn.org/)                                         | "Uvicorn is an ASGI web server implementation for Python" |
| [render](https://docs.render.com/)                                          | "Render is a unified cloud to build and run all your apps and websites" |
| [python-dotenv](https://pypi.org/project/python-dotenv/)                    | "Python-dotenv reads key-value pairs from a .env file and can set them as environment variables" |
| [pymongo](https://pymongo.readthedocs.io/en/stable/)                        | "PyMongo is a Python distribution containing tools for working with MongoDB"|


### Example of .env (see .env.sample)
| Variables                      |
|-------------------------------|
| USERNAME = 'username in MongoDB database'|
| PASSWORD = 'password in MongoDB database'|
| DB = 'cluster...'|

### Start the application
<pre>
# fill .env with your values

# start the application
$ make start

# Open http://127.0.0.1:8000/
</pre>